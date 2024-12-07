from django.contrib import admin

# TODO configure admin panel
from .models import Cart, CartItems

admin.site.register(Cart)
admin.site.register(CartItems)
