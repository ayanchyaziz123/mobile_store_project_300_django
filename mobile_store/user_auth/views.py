from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from user_panel.models import *
from user_panel. utils import cartData, cookieCart, guestOrder
# Create your views here.

def logIn(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()
    context = {
    'products': products,
    'items': items,
    'order': order,
    'cartItems': cartItems,
         }
   
    if request.method == "POST":
        user_name = request.POST['user_name']
        password = request.POST['password']
        user = authenticate(username=user_name, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in')
            return redirect('user_home')
        else:
            messages.error(request, 'Not logged in')
            return render(request, 'user_panel/login.html', context)

    else:  
        return render(request, 'user_panel/login.html', context)  


def create_account(request):
    return render(request, 'user_panel/create_account.html', context)
    

def logOut(request):
    logout(request)
    messages.success(request, 'Logged out')
    return redirect('user_home')


def userSignUp(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()
    
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
               login(request, user)  
            return redirect('user_home')
        else:
            context  = {'form' : form,
               }
    else:  # GET request
        form = UserCreationForm()
        context  = {'form' : form,
                   'products': products,
                   'items': items,
                    'order': order,
                    'cartItems': cartItems,
                   }

    return render(request, 'user_panel/create_account.html', context)
