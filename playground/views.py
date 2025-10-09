from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'playground/home.html', { 'products': products })

def say_hello(request):
    return render(request, 'playground/hello.html', {'name': 'Zoro'})