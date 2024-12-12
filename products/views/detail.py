from django.http import JsonResponse
from django.shortcuts import redirect, render

from ..models import Product, ProductIMG, ProductVariation


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
