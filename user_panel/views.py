from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
     return render(request, 'user_panel/home.html')  
def store(request):
     return render(request, 'user_panel/store.html')     
def cart(request):
     return render(request, 'user_panel/cart.html') 
def checkout(request):
     return render(request, 'user_panel/checkout.html')                  
