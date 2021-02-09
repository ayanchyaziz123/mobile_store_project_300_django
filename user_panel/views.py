from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
     return render(request, 'user_panel/home.html')  
def store(request):
     products = Product.objects.all()
     context = {}
     context = {
          'products': products,
     }
     return render(request, 'user_panel/store.html', context)     
def cart(request):
     return render(request, 'user_panel/cart.html') 
def checkout(request):
     return render(request, 'user_panel/checkout.html')                  
