from django.urls import path

from .views import add_cart_item, cart, remove_cart_item, delete_cart_item

urlpatterns = [
    path("", cart, name="cart_page"),
    path("add/", add_cart_item, name="add_cart"),
    path("remove/", remove_cart_item, name="remove_cart"),
    path("delete/", delete_cart_item, name="delete_cart"),
]
