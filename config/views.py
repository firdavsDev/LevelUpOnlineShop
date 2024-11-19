from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from products.models import Product

"""
1) HttpResponse - Bu bizga HTTP status code va String (HTML) contentni qaytaradi.
2) JsonResponse - Bu bizga JSON contentni qaytaradi. (dict)
3) render(request, file_name.html) - Bu bizga HTML faylni qaytaradi. (html)

"""


def home_page(request):
    products = Product.objects.all()
    context = {"hello": "Hello World", "number": 123, "products": products}
    return render(request, "index.html", context)
