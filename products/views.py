from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect, render

from .models import Product, ProductIMG, ProductVariation, Size


def product_list(request):

    # Qidiruv so'rovlari
    search = request.GET.get(
        "search", ""
    ).strip()  # Qidiruv uchun foydalanuvchi kiritgan ma'lumot
    category_id = request.GET.get("category_id", "")  # Kategoriya ID'si
    size_id = request.GET.get("size_id", "")  # O'lcham ID'si

    # Filter prices
    min_price = request.GET.get("min_price", "")
    max_price = request.GET.get("max_price", "")

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
            # variations__price__range=[min, max],  # TODO Narx oraliqi filterini qushish
        ).distinct()  # here variations is the related name of ProductVariation model

    if min_price and max_price:
        min_price = int(min_price)
        max_price = int(max_price)
        if min_price <= max_price:
            products = products.filter(
                variations__price__range=[min_price, max_price]
            )

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
        "size_variations": size_variations,  # O'lcham variatsiyalari
        "products": products,
        "page_size": page_size,
    }

    return render(request, "store/products.html", context)


def product_detail(request, product_id):
    try:
        # Mahsulotni ID bo'yicha olish
        product = Product.objects.get(id=product_id, is_active=True)

        # Mahsulotga tegishli boshqa ma'lumotlar
        product_images = ProductIMG.objects.filter(product=product)

        # Mahsulotning variatsiyalari
        product_variations = ProductVariation.objects.filter(product=product)

        # O'lcham va rang variatsiyalari
        size_variations = product_variations.values("size__name", "size__id").distinct()

        # AJAX so'rovlari uchun
        size_id = request.GET.get("size_id", "")
        color_id = request.GET.get("color_id", "")

        if size_id and color_id:
            # product variant
            product_variant = product_variations.filter(
                size__id=size_id, color__id=color_id
            ).first()
            # filter product variations by color id and size id
            product_variant_price = product_variant.price
            # stock = product_variations.filter(size__id=size_id, color__id=color_id).first().stock
            product_variant_stock = product_variant.stock
            context = {
                "product_variant_price": product_variant_price,
                "product_variant_stock": product_variant_stock,
            }
            return JsonResponse(context, safe=False)

        if size_id:
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
        }

        return render(request, "store/product-detail.html", context)

    except Product.DoesNotExist:
        return redirect("store")  # Mahsulot topilmasa, asosiy sahifaga qaytish
