from django.urls import path

from .views import product_detail, products

urlpatterns = [
    path("", products, name="store"),
    path("<int:product_id>/", product_detail, name="product_detail"),
]
