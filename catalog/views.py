from django.shortcuts import render
from catalog.models import Categories

def catalog(request):
    return render(request, 'catalog/catalog.html')

def product(request):
    return render(request, 'catalog/product.html')
