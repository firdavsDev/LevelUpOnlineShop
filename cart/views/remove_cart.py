from django.shortcuts import redirect

from products.models import ProductVariation

from ..models import Cart, CartItems


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