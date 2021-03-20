from django.urls import path
from . import views


urlpatterns = [
    path('user_contact/', views.contact, name="user_contact"),
    path('chat_contact/', views.chat_contact, name="chat_contact"),
    path('price_prediction/', views.price_prediction, name="price_prediction"),
]
