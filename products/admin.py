from django.contrib import admin

# Register your models here.
from .models import Category, Color, Product, ProductIMG, ProductVariation, Size, Brand, Season

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


class BrandAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["is_active"]
    search_fields = ["name"]
    date_hierarchy = "created_at"


admin.site.register(Brand, BrandAdmin)


class SeasonAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["is_active"]
    search_fields = ["name"]
    date_hierarchy = "created_at"


admin.site.register(Season, SeasonAdmin)


# imges tuburline
class ProductIMGInline(admin.TabularInline):
    model = ProductIMG
    extra = 1  # qancha qo'shishni ko'rsatadi
    min_num = 1  # qancha minimal qo'shishni ko'rsatadi
    max_num = 5  # qancha maksimal qo'shishni ko'rsatadi


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "category",
        "brand",
        "is_active",
        "created_at",
        "updated_at",
    ]
    list_filter = ["category", "is_active"]
    search_fields = ["name"]
    date_hierarchy = "created_at"
    list_editable = ["is_active"]
    inlines = [ProductIMGInline]
    autocomplete_fields = [
        "category",
        "brand",
        "season",
    ] 


admin.site.register(Product, ProductAdmin)


class ProductIMGAdmin(admin.ModelAdmin):
    list_display = ["product", "image", "created_at", "updated_at"]
    list_filter = ["product"]
    search_fields = [
        "product__name"
    ]  # __ bu 2 ta underscore bilan ishlatiladi. yani product__name bu product modeldagi name fieldini izlaydi
    date_hierarchy = "created_at"
    autocomplete_fields = [
        "product",
    ] 


admin.site.register(ProductIMG, ProductIMGAdmin)


class ColorAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    # date_hierarchy = "created_at"


admin.site.register(Color, ColorAdmin)


class SizeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    date_hierarchy = "created_at"


admin.site.register(Size, SizeAdmin)


class ProductVariationAdmin(admin.ModelAdmin):
    list_display = [
        "product",
        "color",
        "size",
        "price",
        "stock",
        "is_active",
        "created_at",
    ]
    search_fields = ["product__name"]
    list_filter = ["product", "color", "size", "is_active"]
    date_hierarchy = "created_at"
    autocomplete_fields = [
        "product",
        "size",
        "color",
    ]  # bu product modelni qidirish imkonini beradi
    list_editable = ["is_active", "stock", "price"]


admin.site.register(ProductVariation, ProductVariationAdmin)
