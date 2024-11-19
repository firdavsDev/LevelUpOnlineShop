from django.contrib import admin

# Register your models here.
from .models import Category, Product

# Simple way
# admin.site.register(Category)
# admin.site.register(Product)


# More beautiful way
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "is_active", "created_at", "updated_at"]
    list_filter = ["is_active"]
    search_fields = ["name"]
    date_hierarchy = "created_at"


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "price",
        "category",
        "stock",
        "is_active",
        "created_at",
        "updated_at",
    ]
    list_filter = ["category", "is_active"]
    search_fields = ["name"]
    date_hierarchy = "created_at"


admin.site.register(Product, ProductAdmin)
