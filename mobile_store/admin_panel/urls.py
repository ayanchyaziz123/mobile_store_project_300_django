from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_panelLogIn, name='admin_panelLogIn'),
    path('admin_home/', views.home, name='admin_home'),
    path('index_product/', views.index_product, name='index_product'),
    path('create_product/', views.create_product, name='create_product'),
]

    