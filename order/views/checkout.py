from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from accounts.models import Profile
from cart.utils import get_user_cart
from common.models import District, Region
from order.models import Delivery, Order

from ..forms import CheckoutFormModel

# from django.views.decorators.cache import cache_page


# @cache_page(60 * 15)
@login_required
def checkout(request):
    user_cart = get_user_cart(request)
    cart_items = user_cart.items.all()
    total_price = sum([item.price for item in cart_items])
    percent = user_cart.percent
    donation = total_price * Decimal(percent)
    grand_total = total_price + donation

    user = request.user
    profile = Profile.objects.get(user=user)
    initial = {
        "region": profile.region,
        "district": profile.district,
        "street": profile.address,
        "phone": profile.phone,
        "email": profile.email,
    }
    order_obj = Order.objects.create(
        customer=profile,
        total_price=total_price,
    )
    order_obj.cart_items.add(cart_items)

    checkout_form = CheckoutFormModel(initial=initial)

    if request.method == "POST":
        checkout_form = CheckoutFormModel(request.POST, initial=initial)
        if checkout_form.is_valid():
            checkout_form.save(order_obj=order_obj)

    context = {
        "cart_items": cart_items,
        "total_price": total_price,
        "donation": round(donation, 2),
        "grand_total": round(grand_total, 2),
        "checkout_form": checkout_form,
    }

    return render(request, "order/checkout.html", context)
