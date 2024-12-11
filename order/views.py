from decimal import Decimal

from django.shortcuts import render

from accounts.models import Profile
from cart.utils import get_user_cart


# Create your views here.
def checkout(request):
    user_cart = get_user_cart(request)
    cart_items = user_cart.items.all()
    # TODO use cache for calculation
    total_price = sum([item.price for item in cart_items])
    # TODO donationi foizini adminkada belgilash
    donation = total_price * Decimal("0.1")
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
