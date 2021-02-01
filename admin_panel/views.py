from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def home(request):
    return render(request, 'admin_panel/home.html')

def index_product(request):
    return render(request, 'admin_panel/products/index.html')
def create_product(request):
    return render(request, 'admin_panel/products/create.html')    

