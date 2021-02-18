from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def logIn(request):
    return render(request, 'user_panel/login.html')

def logOut(request):
    logout(request)
    messages.success(request, 'Logged out')
    return redirect('user_home')