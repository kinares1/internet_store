from django.contrib import admin
from .models import Product, Category, User, Order
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Order)
