from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from user_panel.models import *
from django.contrib.auth.models import User

# Create your views here.

def contact(request):
    if request.user.is_authenticated:
        user_name = request.user.username          
        chat = Chat.objects.filter(user_name=user_name) 
        context = {
                'Chat':chat,
            }
        return render(request, 'user_panel/contact.html', context)     

    else: 
        return render(request, 'user_panel/login.html')   

def chat_contact(request):
    print("hello world")
    user_name = request.user.username    
    print(request.method)
    if request.is_ajax():
        print("hello world")
        um = request.POST.get('user_messages', None)
        cm = request.POST.get('chatbot_messages', None)
        if um and cm:
            data  = Chat(user_name=user_name, user_message=um, chatbot_message=cm)
            data.save()
            response = {
                         'msg':'Your form has been submitted successfully' # response message
            }
            return JsonResponse(response) # return response as JSON
                     
    chat = Chat.objects.filter(user_name=user_name) 
    context = {
                'Chat':chat,
            }
    return render(request, 'user_panel/contact.html', context)


            