from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.contrib.auth.models import User
import json
import datetime
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from django.core.paginator import Paginator
from . utils import cartData, cookieCart, guestOrder


#
# Create your views here.


def home(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()
    context = {}
    context = {
        'products': products,
        'items': items,
        'order': order,
        'cartItems': cartItems,
    }
    return render(request, 'user_panel/home.html', context)


def store(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {}
    context = {
        'products': products,
        'items': items,
        'order': order,
        'cartItems': cartItems,
    }
    return render(request, 'user_panel/store.html', context)


def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems

    }
    return render(request, 'user_panel/cart.html', context)


@csrf_protect
def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,

    }
    return render(request, 'user_panel/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print("product id", productId)
    print("action :", action)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse("item was added", safe=False)


@csrf_protect
def processOrder(request):
    print('Data', request.body)
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],


        )

    return JsonResponse("payment complete", safe=False)


def serach(request):
    query = request.GET['search']
    if query == "":
        Pro = ""
    else:
        Pro = Product.objects.filter(
            Q(name__icontains=query) | Q(price__contains=query))

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()
    tot = Pro.count()
    context = {}
    context = {
        'products': products,
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'pro': Pro,
        'query': query,
        'tot': tot,
    }
    return render(request, 'user_panel/search.html', context)


def view(request, slug):
    Pro = Product.objects.filter(id=slug).first()
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()
    context = {}
    context = {
        'products': products,
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'pro': Pro,

    }
    return render(request, 'user_panel/view.html', context)



    



