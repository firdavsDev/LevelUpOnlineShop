from django.contrib import admin

# Register your models here.
from .models import Category, Product, ProductIMG

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


# imges tuburline
class ProductIMGInline(admin.TabularInline):
    model = ProductIMG
    extra = 1  # qancha qo'shishni ko'rsatadi
    min_num = 1  # qancha minimal qo'shishni ko'rsatadi
    max_num = 5  # qancha maksimal qo'shishni ko'rsatadi


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
    list_editable = ["price", "stock", "is_active"]
    inlines = [ProductIMGInline]


admin.site.register(Product, ProductAdmin)


class ProductIMGAdmin(admin.ModelAdmin):
    list_display = ["product", "image", "created_at", "updated_at"]
    list_filter = ["product"]
    search_fields = [
        "product__name"
    ]  # __ bu 2 ta underscore bilan ishlatiladi. yani product__name bu product modeldagi name fieldini izlaydi
    date_hierarchy = "created_at"


admin.site.register(ProductIMG, ProductIMGAdmin)
