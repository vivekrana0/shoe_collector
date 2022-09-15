from django.shortcuts import render
from django.http import HttpResponse
from .models import Shoe
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.



def home(request):
    return HttpResponse('<h1>Welcome to my Sneaker Collection</h1>')

def about(request):
    return render(request, 'about.html')

def shoes_index(request):
    shoes = Shoe.objects.all()
    return  render(request, 'shoes/index.html', {'shoes': shoes})

def shoe_detail(request, shoe_id):
    shoe = Shoe.objects.get(id=shoe_id)
    print(f"{shoe} id is {shoe_id} this is the object")
    return render(request, 'shoes/details.html',{'shoe':shoe})

class ShoeCreate(CreateView):
    model = Shoe
    fields = '__all__'

class ShoeUpdate(UpdateView):
    model = Shoe
    fields = ['brand', 'description', 'year']

class ShoeDelete(DeleteView):
    model = Shoe
    success_url = '/shoes/'
