from django.http import HttpResponse, JsonResponse

# html render
from django.shortcuts import render

from products.models import Product, ProductVariation

"""
1) HttpResponse - Bu bizga HTTP status code va String (HTML) contentni qaytaradi.
2) JsonResponse - Bu bizga JSON contentni qaytaradi. (dict)
3) render(request, file_name.html) - Bu bizga HTML faylni qaytaradi. (html)

"""


def home_page(request):
    # products = Product.objects.variations.all() # Bu usulda chaqirish mumkin emas.
    # 2 xil usulda chaqirish mumkin. select_related(related_name) va prefetch_related()
    products = Product.objects.filter(is_active=True)
    context = {"products": products}
    return render(request, "index.html", context)
