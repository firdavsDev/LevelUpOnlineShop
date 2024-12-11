from decimal import Decimal

from django.contrib import messages
from django.shortcuts import redirect, render

from products.models import ProductVariation

from .models import Cart, CartItems
from .utils import get_session_key, get_user_cart


def cart(request):
    user_cart = get_user_cart(request)

    cart_items = CartItems.objects.filter(cart=user_cart)
    total_price = 0
    for item in cart_items:
        total_price += item.price

    # doanytion is 10% of total price
    donation = total_price * Decimal("0.1")
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
        print("POST")
        size_id = request.POST.get("size_id")
        product_id = request.POST.get("product_id")
        color_id = request.POST.get("color_id")
        product_variant = ProductVariation.objects.get(
            product_id=product_id, size_id=size_id, color_id=color_id
        )
        cart_item, created = CartItems.objects.get_or_create(
            cart=user_cart, product_variant=product_variant
        )
        print("created", created)
        if cart_item.product_variant.stock != 0:
            if not created:
                cart_item.quantity += 1
                cart_item.save()
        else:
            messages.error(request, "Bu mahsulot bazamizda qolmadi")

    return redirect("cart_page")


def remove_cart_item(request):
    user_cart = Cart.objects.get(user=request.user)
    if request.method == "POST":
        product_variant_id = request.POST.get("product_variant_id")
        cart_item = CartItems.objects.get(
            cart=user_cart, product_variant__id=product_variant_id
        )
        cart_item.quantity -= 1
        if cart_item.quantity == 0:
            cart_item.delete()
        else:
            cart_item.save()
    return redirect("cart_page")


def delete_cart_item(request):
    user_cart = Cart.objects.get(user=request.user)
    if request.method == "POST":
        product_variant_id = request.POST.get("product_variant_id")
        cart_item = CartItems.objects.get(
            cart=user_cart, product_variant__id=product_variant_id
        )
        cart_item.delete()

    return redirect("cart_page")
