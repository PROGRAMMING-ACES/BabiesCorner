from django.contrib import admin
from .models import Category, Brand, Product, ShippingAddress, OrderItem, Order

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(ShippingAddress)
admin.site.register(OrderItem)
admin.site.register(Order) 