from django.contrib import admin
from .models import Order, Delivery


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ["customer", "status", "total_price","is_active"]
    list_filter = ["is_active"]
    search_fields = ["customer"]
    date_hierarchy = "created_at"
    autocomplete_fields = [
        "cart_items",
    ] 


admin.site.register(Order, OrderAdmin)


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ["order", "phone", "email", "region", "district","is_active"]
    list_filter = ["is_active"]
    search_fields = ["order"]
    date_hierarchy = "created_at"
    autocomplete_fields = [
        "order",
        "region",
        "district",
    ] 


admin.site.register(Delivery, DeliveryAdmin)
