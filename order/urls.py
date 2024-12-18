from django.urls import path

from .views import checkout, order_list, payment

urlpatterns = [
    # Order URLs
    path("list/", order_list, name="my_order_list"),
    path("checkout/", checkout, name="checkout"),
    path("payment/", payment, name="payment"),
]
