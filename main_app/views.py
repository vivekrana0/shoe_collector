from ast import Del
from typing import List
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Shoe, Cloth
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .form import ReasonForm

# Create your views here.



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def shoes_index(request):
    shoes = Shoe.objects.all()
    return  render(request, 'shoes/index.html', {'shoes': shoes})

def shoe_detail(request, shoe_id):
    shoe = Shoe.objects.get(id=shoe_id)
    remaining_cloths = Cloth.objects.exclude(id__in = shoe.cloths.all().values_list('id'))
    reason_form = ReasonForm()
    return render(request, 'shoes/details.html',{'shoe':shoe, 'reason_form': reason_form, 'cloths': remaining_cloths})

class ShoeCreate(CreateView):
    model = Shoe
    fields = '__all__'

class ShoeUpdate(UpdateView):
    model = Shoe
    fields = ['brand', 'description', 'year']

class ShoeDelete(DeleteView):
    model = Shoe
    success_url = '/shoes/'


def add_reason(request, shoe_id):
    form = ReasonForm(request.POST)

    if form.is_valid():
        new_reason = form.save(commit=False)
        new_reason.shoe_id = shoe_id
        new_reason.save()
    return redirect('detail', shoe_id=shoe_id)

class ClothList(ListView):
    model = Cloth

class ClothCreate(CreateView):
    model = Cloth
    fields = '__all__'

class ClothDetails(DetailView):
    model = Cloth

class ClothUpdate(UpdateView):
    model = Cloth
    fields = ['name', 'color']

class ClothDelete(DeleteView):
    model = Cloth
    success_url = '/cloths/'


def add_attribute(request, shoe_id, cloth_id):
    cloth = Cloth.objects.get(id=cloth_id)
    shoe = Shoe.objects.get(id=shoe_id)
    shoe.cloths.add(cloth)
    return redirect('detail', shoe_id=shoe_id)

def remove_attribute(request, shoe_id, cloth_id):
    Shoe.objects.get(id=shoe_id).cloths.remove(cloth_id)
    return redirect('detail', shoe_id=shoe_id)