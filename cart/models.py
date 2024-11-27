from django.db import models

from accounts.models import CustomUser
from common.models import BaseModel
from products.models import ProductVariation


class CartItems(BaseModel):
    product_variant = models.ForeignKey(ProductVariation, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    # price = product_variant.price * quantity
    # TODO Fk from items to cart

    # TODO class Meta:


class Cart(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    cart_items = models.ManyToManyField(CartItems, blank=True)

    # TODO meta
