from django.db import models

from accounts.models import CustomUser
from common.models import BaseModel
from products.models import ProductVariation


class Cart(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Kartalar"
        verbose_name = "Karta"

class CartItems(BaseModel):
    product_variant = models.ForeignKey(ProductVariation, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    # price = product_variant.price * quantity
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="cart_items"
    )

    class Meta:
        verbose_name_plural = "Karta elementlari"
        verbose_name = "Karta elementi"