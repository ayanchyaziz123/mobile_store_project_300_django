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
    ord = []
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = []

    context = {
        'items': items,
        'order': order,

    }
    return render(request, 'user_panel/cart.html', context)


def checkout(request):
    return render(request, 'user_panel/checkout.html')
