from django.urls import path

from .views import add_cart, cart

urlpatterns = [
    path("", cart, name="cart_page"),
    path("add/", add_cart, name="add_cart"),
]
