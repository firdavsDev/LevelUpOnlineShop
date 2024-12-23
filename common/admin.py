from django.contrib import admin

from .models import District, Region

# Add costom admin site header
admin.site.site_header = "Costom Admin"
admin.site.site_title = "Costom Admin Portal"
admin.site.index_title = "Welcome to Costom Admin Portal"


class RegionAdmin(admin.ModelAdmin):
    list_display = ["name", "is_active", "created_at", "updated_at"]
    list_filter = ["is_active"]
    search_fields = ["name"]
    date_hierarchy = "created_at"


admin.site.register(Region, RegionAdmin)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ["name", "is_active", "created_at", "updated_at"]
    list_filter = ["is_active"]
    search_fields = ["name"]
    date_hierarchy = "created_at"
    autocomplete_fields = ["region"]


admin.site.register(District, DistrictAdmin)
