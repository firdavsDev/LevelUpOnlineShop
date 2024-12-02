from django.contrib import admin

# TODO Register your models here.
from .models import Cart, CartItems


class CartAdmin(admin.ModelAdmin):
    list_display = [
        "user"
    ]
    search_fields = ["user"]
    date_hierarchy = "created_at"
    list_editable = ["is_active"]

admin.site.register(CartAdmin, Cart)

class CartItemsAdmin(admin.ModelAdmin):
    list_display = [
        "product_variant",
        "quantity",
        "cart",
    ]
    search_fields = ["cart"]
    date_hierarchy = "created_at"
    list_editable = ["is_active"]


admin.site.register(CartItemsAdmin, CartItems)