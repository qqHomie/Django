from django.shortcuts import render
from .models import Product, ProductCategory

# Create your views here.

def index(request):
    context = {
        'title': 'StoreApp',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'storeProducts/index.html', context)

def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'storeProducts/products.html', context)