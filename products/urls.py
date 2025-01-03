from django.urls import path

from .views import product_detail, product_list

urlpatterns = [
    path("", product_list, name="store"),
    path("<int:product_id>/", product_detail, name="product_detail"),
]