from django.urls import path
from . import views


urlpatterns = [
    path('user_login/', views.logIn, name="user_login"),
    path('user_logout/', views.logOut, name="user_logout"),
    path('user_create_account/', views.create_account, name="user_create_account"),
]
