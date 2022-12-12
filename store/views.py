from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def index(request):
    Products = Product.get_all_products
    print(Products)
    return render(request, 'index.html')