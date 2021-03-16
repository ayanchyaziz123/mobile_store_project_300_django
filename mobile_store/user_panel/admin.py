from django.contrib import admin

# Register your models here.
from .models import Customer, Product, Order, OrderItem, ShippingAddress, Chat

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Chat)

