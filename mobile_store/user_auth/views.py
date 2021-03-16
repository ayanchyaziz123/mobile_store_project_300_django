from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

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



    

def logOut(request):
    logout(request)
    messages.success(request, 'Logged out')
    return redirect('user_home')