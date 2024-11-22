from django.db.models import (
    Q,  # Q() class ni import qilamiz chunki bizga or va and operatorlar kerak
)
from django.shortcuts import redirect, render

from .models import Category, Product, ProductIMG


def product_list(request):
    products = Product.objects.filter(
        is_active=True
    )  # SQL query: SELECT * FROM product WHERE is_active = True
    categories = Category.objects.filter(is_active=True)
    # search
    search = request.GET.get("search", "")
    category_id = request.GET.get("category_id", "")
    if category_id != "":
        products = products.filter(category__id=category_id)
    if search != "":
        # __icontains bu field ni ichida qidirish
        # products = products.filter(name__icontains=search, description__icontains=search)

        # Q() class ni ichida qidirish, | or, & and
        products = products.filter(
            Q(name__icontains=search) | Q(description__icontains=search)
        )

    context = {
        "products": products,
        "search": search,
        "category_id": category_id,
        "categories": categories,
    }

    return render(request, "store/products.html", context)


def product_detail(request, product_id):
    try:
        # product_id bu url dan kelgan qiymat bo'ladi
        product = Product.objects.get(
            id=product_id, is_active=True
        )  # get(field1=value, field_n=value) methodi faqatgina 1 ta qiymat qaytaradi
        product_images = ProductIMG.objects.filter(product=product)
        context = {"product": product, "product_images": product_images}
        return render(request, "store/product-detail.html", context=context)
    except Product.DoesNotExist:
        context = {"product": product, "product_images": product_images}
        return redirect("store", context=context)
