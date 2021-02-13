from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
import datetime
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q


# Create your views here.


def home(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

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
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {}
    context = {
        'products': products,
        'items': items,
        'order': order,
        'cartItems': cartItems,
    }
    return render(request, 'user_panel/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items': 0,  'shipping': False}
        cartItems = order['get_cart_items']

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems

    }
    return render(request, 'user_panel/cart.html', context)

@csrf_protect
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items': 0,  'shipping': False}
        cartItems = order['get_cart_items']

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
    print("action :" , action)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

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
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()   
    if order.shipping == True:
        ShippingAddress.objects.create(
            customer = customer,
            order = order,
            address = data['shipping']['address'],
            city = data['shipping']['city'],
            state = data['shipping']['state'],
            zipcode = data['shipping']['zipcode'],


        )     

    else:
        print("user is not logged in")    
    return JsonResponse("payment complete", safe=False)

def serach(request):
    query = request.GET['search']
    if query =="":
        Pro = ""
    else:
        Pro = Product.objects.filter(Q(name__icontains=query) | Q(price__contains=query))
     


    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {}
    context = {
        'products': products,
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'pro':Pro,
        'query':query
    }
    return render(request, 'user_panel/search.html', context)
