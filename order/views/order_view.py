from decimal import Decimal

from django.shortcuts import render

from accounts.models import Profile
from cart.utils import get_user_cart

from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def checkout(request):
    user_cart = get_user_cart(request)
    cart_items = user_cart.items.all()
    total_price = sum([item.price for item in cart_items])
    percent = user_cart.percent
    donation = total_price * Decimal(percent)
    grand_total = total_price + donation
    user_profile = Profile.objects.get(user=request.user)

    context = {
        "cart_items": cart_items,
        "total_price": total_price,
        "donation": round(donation, 2),
        "grand_total": round(grand_total, 2),
        "user_profile": user_profile,
    }

    return render(request, "order/checkout.html", context)
