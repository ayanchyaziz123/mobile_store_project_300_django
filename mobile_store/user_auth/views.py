from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def logIn(request):
   
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
            return render(request, 'user_panel/login.html')

    else:  
        return render(request, 'user_panel/login.html')  


def create_account(request):
    return render(request, 'user_panel/create_account.html')
    

def logOut(request):
    logout(request)
    messages.success(request, 'Logged out')
    return redirect('user_home')


def userSignUp(request):
    
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)  
            return redirect('user_home')
        else:
            context  = {'form' : form,
               }
    else:  # GET request
        form = UserCreationForm()
        context  = {'form' : form,
                   }

    return render(request, 'user_panel/create_account.html', context)
