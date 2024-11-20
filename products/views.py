from django.shortcuts import render
from .models import Product, Category


def store(request):
    products = Product.objects.all()
    categorys = Category.objects.all()
    return render(request, "store.html", context={
        'products': products,
        'categorys': categorys
    })