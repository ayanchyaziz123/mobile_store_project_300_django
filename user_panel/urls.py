from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="user_home"),
    path('user_store/', views.store, name="user_store"),
    path('user_cart/', views.cart, name="user_cart"),
    path('user_checkout/', views.checkout, name="user_checkout"),
    path('user_update_item/', views.updateItem, name="user_update_item"),
    path('user_process_order/', views.processOrder, name="user_process_order"),
    path('user_search/', views.serach, name="user_search"),
    path('user_view/<str:slug>', views.view, name="user_view"),
]
