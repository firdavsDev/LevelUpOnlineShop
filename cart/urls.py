from django.urls import path

from .views import add_cart, cart, remove_cart, delete_cart

urlpatterns = [
    path("", cart, name="cart_page"),
    path("add/", add_cart, name="add_cart"),
    path("remove/", remove_cart, name="remove_cart"),
    path("delete/", delete_cart, name="delete_cart"),
]
