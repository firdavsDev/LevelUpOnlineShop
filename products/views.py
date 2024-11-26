from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.core.paginator import Paginator

from .models import Product, ProductIMG, ProductVariation


def product_list(request):
    # Mahsulotlarni faqat aktiv holatini olish
    products = Product.objects.filter(is_active=True)

    # Qidiruv so'rovlari
    search = request.GET.get("search", "").strip()  # Qidiruv uchun foydalanuvchi kiritgan ma'lumot
    category_id = request.GET.get("category_id", "")  # Kategoriya ID'si

    # Kategoriya filtri
    if category_id:
        products = products.filter(category__id=category_id)

    # Qidiruv filtri
    if search:
        products = products.filter(Q(name__icontains=search) | Q(description__icontains=search))

    # Pagination (sahifalash)
    paginator = Paginator(products, 2)  # Har bir sahifada 12 ta mahsulot
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Variatsiyalar
    product_variations = ProductVariation.objects.all()
    size_variations = product_variations.values("size__name", "size__id").distinct()

    context = {
        "page_obj": page_obj,  # Sahifa obyekti (faqat hozirgi sahifa ma'lumotlari)
        "search": search,  # Qidiruv qiymati
        "category_id": category_id,  # Kategoriya qiymati
        "size_variations": size_variations,  # O'lcham variatsiyalari
    }

    return render(request, "store/products.html", context)


def product_detail(request, product_id):
    try:
        # Mahsulotni ID bo'yicha olish
        product = Product.objects.get(id=product_id, is_active=True)

        # Mahsulotga tegishli boshqa ma'lumotlar
        product_images = ProductIMG.objects.filter(product=product)
        product_variations = ProductVariation.objects.filter(product=product)

        # O'lcham va rang variatsiyalari
        size_variations = product_variations.values("size__name", "size__id").distinct()
        color_variations = product_variations.values("color__name", "color__id").distinct()

        # AJAX so'rovlari uchun
        size_id = request.GET.get("size_id", "")
        color_id = request.GET.get("color_id", "")

        if size_id:
            return JsonResponse(
                list(
                    product_variations.filter(size__id=size_id).values(
                        "color__name", "color__id"
                    )
                ),
                safe=False,
            )

        if color_id:
            return JsonResponse(
                list(
                    product_variations.filter(color__id=color_id).values(
                        "price", "id"
                    )
                ),
                safe=False,
            )

        context = {
            "product": product,
            "product_images": product_images,
            "size_variations": size_variations,
            "color_variations": color_variations,
        }

        return render(request, "store/product-detail.html", context)

    except Product.DoesNotExist:
        return redirect("store")  # Mahsulot topilmasa, asosiy sahifaga qaytish
