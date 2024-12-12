from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from ..models import Product, ProductVariation


def product_list(request):

    # Qidiruv so'rovlari
    search = request.GET.get(
        "search", ""
    ).strip()  # Qidiruv uchun foydalanuvchi kiritgan ma'lumot
    category_id = request.GET.get("category_id", "")  # Kategoriya ID'si
    size_id = request.GET.get("size_id", "")  # O'lcham ID'si
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")

    # pagination query
    page_number = request.GET.get("page", 1)
    page_size = request.GET.get("page-size", 10)

    # Mahsulotlarni faqat aktiv holatini olish
    products = Product.objects.filter(is_active=True)

    # Kategoriya filtri
    if category_id:
        products = products.filter(category__id=category_id)

    # Qidiruv filtri
    if search:
        products = products.filter(
            Q(name__icontains=search) | Q(description__icontains=search)
        )

    # O'lcham filtri
    if size_id:
        products = products.filter(
            variations__size_id=size_id,
        ).distinct()  # here variations is the related name of ProductVariation model

    if min_price and max_price:
        products = products.filter(
            variations__price__range=[
                min_price,
                max_price,
            ]  # __range create_at__range=[now, 30dayago]
        ).distinct()  # here variations is the related name of ProductVariation model

    # Variatsiyalar
    product_variations = ProductVariation.objects.filter(is_active=True)
    size_variations = product_variations.values("size__id", "size__name").distinct()

    # Pagination (sahifalash)
    paginator = Paginator(products, page_size)  # Har bir sahifada 12 ta mahsulot
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,  # Sahifa obyekti (faqat hozirgi sahifa ma'lumotlari)
        "search": search,  # Qidiruv qiymati
        "category_id": category_id,  # Kategoriya qiymati
        "size_id": size_id,  # O'lcham qiymati
        "size_variations": size_variations,  # O'lcham variatsiyalari
        "page_size": page_size,
    }

    return render(request, "store/products.html", context)