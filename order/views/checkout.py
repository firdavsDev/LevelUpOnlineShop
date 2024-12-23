from decimal import Decimal

from django.shortcuts import render

from accounts.models import Profile
from cart.utils import get_user_cart
from common.models import District, Region

# from django.views.decorators.cache import cache_page

from common.models import District, Region
from order.models import Delivery, Order

# @cache_page(60 * 15)
def checkout(request):
    user_cart = get_user_cart(request)
    cart_items = user_cart.items.all()
    total_price = sum([item.price for item in cart_items])
    percent = user_cart.percent
    donation = total_price * Decimal(percent)
    grand_total = total_price + donation
    user_profile = Profile.objects.get(user=request.user)
    order = Order.objects.get(customer__user = request.user)
    regions = Region.objects.all()
    districts = District.objects.all()

    if request.method == "POST":
        region_id = request.POST.get("region")
        district_id = request.POST.get("district")
        street = request.POST.get("street")
        building = request.POST.get("building")
        house = request.POST.get("house")
        postal_code = request.POST.get("postal_code")
        phone = request.POST.get("phone")
        email = request.POST.get("email")

        region_obj = regions.get(id = region_id)
        district_obj = districts.get(id = district_id)
        delivery_obj = Delivery.objects.create(
            order = order,
            region = region_obj,
            district = district_obj,
            street = street,
            building = building,
            house = house,
            postal_code = postal_code,
            phone = phone,
            email = email
            )
        

    context = {
        "cart_items": cart_items,
        "regions": Region.objects.filter(is_active=True),
        "districts": District.objects.filter(is_active=True),
        "total_price": total_price,
        "donation": round(donation, 2),
        "grand_total": round(grand_total, 2),
        "user_profile": user_profile,
        "regions": regions,
        "districts": districts,
    }

    return render(request, "order/checkout.html", context)
