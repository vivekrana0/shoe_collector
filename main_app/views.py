
import imp
from urllib import request
from urllib.robotparser import RequestRate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Shoe, Cloth
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .form import ReasonForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def shoes_index(request):
    shoes = Shoe.objects.filter(user=request.user)
    return  render(request, 'shoes/index.html', {'shoes': shoes})

@login_required 
def shoe_detail(request, shoe_id):
    shoe = Shoe.objects.get(id=shoe_id)
    if shoe.user == request.user:
        remaining_cloths = Cloth.objects.exclude(id__in = shoe.cloths.all().values_list('id'))
        reason_form = ReasonForm()
        return render(request, 'shoes/details.html',{'shoe':shoe, 'reason_form': reason_form, 'cloths': remaining_cloths})
    else:
        return HttpResponse("<h1>Invalid input, 404</h1>")

class ShoeCreate(LoginRequiredMixin, CreateView):
    model = Shoe
    fields = ['name', 'brand', 'year', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ShoeUpdate(LoginRequiredMixin, UpdateView):
    model = Shoe
    fields = ['brand', 'description', 'year']

class ShoeDelete(LoginRequiredMixin, DeleteView):
    model = Shoe
    success_url = '/shoes/'


@login_required
def add_reason(request, shoe_id):
    form = ReasonForm(request.POST)

    if form.is_valid():
        new_reason = form.save(commit=False)
        new_reason.shoe_id = shoe_id
        new_reason.save()
    return redirect('detail', shoe_id=shoe_id)

class ClothList(LoginRequiredMixin, ListView):
    model = Cloth

    def get_queryset(self):
        return Cloth.objects.filter(user = self.request.user)
    

class ClothCreate(LoginRequiredMixin, CreateView):
    model = Cloth
    fields = ['name', 'color']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ClothDetails(LoginRequiredMixin, DetailView):
    model = Cloth

    def get_queryset(self):
        return Cloth.objects.filter(user=self.request.user)

class ClothUpdate(LoginRequiredMixin, UpdateView):
    model = Cloth
    fields = ['name', 'color']

class ClothDelete(LoginRequiredMixin, DeleteView):
    model = Cloth
    success_url = '/cloths/'

@login_required
def add_attribute(request, shoe_id, cloth_id):
    cloth = Cloth.objects.get(id=cloth_id)
    shoe = Shoe.objects.get(id=shoe_id)
    shoe.cloths.add(cloth)
    return redirect('detail', shoe_id=shoe_id)

@login_required
def remove_attribute(request, shoe_id, cloth_id):
    Shoe.objects.get(id=shoe_id).cloths.remove(cloth_id)
    return redirect('detail', shoe_id=shoe_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid Input'
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form, 'error_message': error_message})