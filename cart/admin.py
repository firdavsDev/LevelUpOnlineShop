from django.contrib import admin

from .models import Cart, CartItems

class CartAdmin(admin.ModelAdmin):
    list_display = ["user", "is_active", "created_at", "updated_at"]
    list_filter = ["is_active"]
    search_fields = ["user"]
    date_hierarchy = "created_at"


class CartItemsAdmin(admin.ModelAdmin):
    list_display = ["cart", "product_variant", "quantity", "is_active", "created_at", "updated_at"]
    list_filter = ["is_active"]
    search_fields = ["quantity"]
    date_hierarchy = "created_at"

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItems, CartItemsAdmin)
