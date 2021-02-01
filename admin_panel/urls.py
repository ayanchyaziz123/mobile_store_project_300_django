from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='admin_home'),
    path('index_product/', views.index_product, name='index_product'),
    path('create_product', views.create_product, name='create_product'),
]

    