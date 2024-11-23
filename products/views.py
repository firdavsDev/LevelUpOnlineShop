from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect, render

from .models import Product, ProductIMG, ProductVariation, Size


def product_list(request):
    products = Product.objects.filter(
        is_active=True
    )  # SQL query: SELECT * FROM product WHERE is_active = True
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
    }

    return render(request, "store/products.html", context)


def product_detail(request, product_id):
    try:
        size_id = request.GET.get("size_id", "")
        # product_id bu url dan kelgan qiymat bo'ladi
        product = Product.objects.get(
            id=product_id, is_active=True
        )  # get(field1=value, field_n=value) methodi faqatgina 1 ta qiymat qaytaradi
        product_images = ProductIMG.objects.filter(product=product)
        product_variations = ProductVariation.objects.filter(product=product)
        size_variations = product_variations.values("size__name", "size__id").distinct()
        if size_id != "":
            return JsonResponse(
                list(
                    product_variations.filter(size__id=size_id).values(
                        "color__name", "color__id"
                    )
                ),
                safe=False,
            )
        context = {
            "product": product,
            "product_images": product_images,
            "size_variations": size_variations,
            "product_id": product_id,
        }
        return render(request, "store/product-detail.html", context=context)
    except Product.DoesNotExist:
        context = {"product": product, "product_images": product_images}
        return redirect("store", context=context)
