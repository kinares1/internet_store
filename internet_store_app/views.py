from django.shortcuts import render, get_object_or_404
from .models import Product, Category, User, Order


def product_list(request):
    products = Product.objects.all()  # Получить все объекты модели Product
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category_detail.html', {'category': category})
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'user_detail.html', {'user': user})
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'order_detail.html', {'order': order})

