from django.contrib import admin

# Register your models here.
# TODO: Register the Order model
from .models import Order

admin.site.register(Order)
