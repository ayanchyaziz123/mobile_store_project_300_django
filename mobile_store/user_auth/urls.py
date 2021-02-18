from django.urls import path
from . import views


urlpatterns = [
    path('user_login/', views.logIn, name="user_login"),
    path('user_logout/', views.logOut, name="user_logout"),
]
