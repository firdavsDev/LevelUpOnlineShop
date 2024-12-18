from django.shortcuts import render

from accounts.models import Profile

from ..models import Order


def create_order(request):
    pass


def order_list(request):
    # status = request.GET.get("status", None)
    # start_date = request.GET.get("start_date", None)
    # end_date = request.GET.get("end_date", None)
    user = request.user
    profile = Profile.objects.get(user=user)
    my_orders = Order.objects.filter(customer=profile)
    context = {"my_orders": my_orders}
    return render(request, "order/order_list.html", context)
