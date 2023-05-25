from django.shortcuts import render, get_object_or_404
from .models import Product, Category, User, Order
def product_list(request):
    products = Product.name.all()
    return render(request, 'product_list.html', {'products': products})
