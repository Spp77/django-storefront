from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def home(request):
    products = Product.objects.all()
    return render(request, 'playground/home.html', { 'products': products })

def say_hello(request):
    return render(request, 'playground/hello.html', {'name': 'Zoro'})


def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "playground/product_create.html", context)

