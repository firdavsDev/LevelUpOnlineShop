from django.contrib import admin

# TODO Register your models here.
from .models import Cart, CartItems

admin.site.register(Cart)
admin.site.register(CartItems)
