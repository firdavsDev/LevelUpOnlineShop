from decimal import Decimal

from django.contrib import messages
from django.shortcuts import redirect, render

from products.models import ProductVariation

from ..models import CartItems
from ..utils import get_user_cart


def cart(request):
    user_cart = get_user_cart(request)

    cart_items = CartItems.objects.filter(cart=user_cart)
    total_price = sum([item.price for item in cart_items])
    # TODO v3 sql annotation & aggregate
    # total_price_v3 = cart_items.aggregate(
    #     total_price=Sum(F("product_variant__price") * F("quantity"))
    # )["total_price"]
    # doanytion is 10% of total price
    percent = user_cart.percent
    donation = total_price * Decimal(percent)
    grand_total = total_price + donation

    context = {
        "cart_items": cart_items,
        "total_price": total_price,
        "donation": round(donation, 2),
        "grand_total": round(grand_total, 2),
    }
    return render(request, "cart/cart.html", context)


def add_cart_item(request):
    # get user cart or create new cart via session key
    user_cart = get_user_cart(request)

    if request.method == "POST":
        size_id = request.POST.get("size_id")
        product_id = request.POST.get("product_id")
        color_id = request.POST.get("color_id")
        # check post data is valid
        if not size_id or not product_id or not color_id:
            messages.error(request, "Maxsulotning xususiyatlarini tanlang!")
            return redirect("product_detail", product_id=product_id)
        product_variant = ProductVariation.objects.get(
            product_id=product_id, size_id=size_id, color_id=color_id
        )
        cart_item, created = CartItems.objects.get_or_create(
            cart=user_cart, product_variant=product_variant
        )
        if cart_item.product_variant.stock != 0:
            if not created:
                cart_item.quantity += 1
                cart_item.save()
        else:
            messages.error(request, "Bu mahsulot bazamizda qolmadi")

    return redirect("cart_page")
