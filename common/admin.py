from django.contrib import admin

from .models import District, Region

# Add costom admin site header
admin.site.site_header = "Costom Admin"
admin.site.site_title = "Costom Admin Portal"
admin.site.index_title = "Welcome to Costom Admin Portal"


# TODO more customization
admin.site.register(Region)
admin.site.register(District)
