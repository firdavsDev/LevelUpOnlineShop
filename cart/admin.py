from django.contrib import admin

from .models import Cart, CartItems


class CartAdmin(admin.ModelAdmin):
    list_display = ["user", "session_key", "is_active", "created_at", "updated_at"]
    list_filter = ["is_active"]
    search_fields = ["user__name"]
    date_hierarchy = "created_at"
    autocomplete_fields = ["user"]


class CartItemsAdmin(admin.ModelAdmin):
    list_display = [
        "cart",
        "product_variant",
        "quantity",
        "is_active",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active"]
    search_fields = ["product_variant__product__name"]
    date_hierarchy = "created_at"
    autocomplete_fields = [
        "cart",
        "product_variant",
    ]


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItems, CartItemsAdmin)
