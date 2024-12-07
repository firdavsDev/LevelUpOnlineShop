from django.db import models

from accounts.models import CustomUser
from common.models import BaseModel
from products.models import ProductVariation


class Cart(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    def __str__(self):
        return f"{self.user.username}'s cart"


class CartItems(BaseModel):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="items", null=True
    )
    product_variant = models.ForeignKey(
        ProductVariation, on_delete=models.CASCADE, null=True
    )
    quantity = models.PositiveSmallIntegerField(default=1)
    # is_ordered = models.BooleanField(default=False)

    @property
    def price(self):
        return self.product_variant.price * self.quantity

    class Meta:
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"
        unique_together = ["product_variant", "cart"]

    def __str__(self):
        return f"{self.cart.user.username} - {self.product_variant.product.name} - {self.quantity}"
