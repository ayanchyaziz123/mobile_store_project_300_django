from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def admin_panelLogIn(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        if email == "admin@gmail.com" and password=="admin123":
            return render(request, 'admin_panel/home.html')  
        else:
            x = "Your pass && email wrong" 
            context = {
                x:x,
            }
            render(request, 'admin_panel/admin_panelLogIn.html', context)     

    return render(request, 'admin_panel/admin_panelLogIn.html')


def home(request):
    return render(request, 'admin_panel/home.html')


def index_product(request):
    return render(request, 'admin_panel/products/index.html')
def create_product(request):
    return render(request, 'admin_panel/products/create.html')    

