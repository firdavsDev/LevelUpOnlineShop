from django.db import models

from accounts.models import Profile
from cart.models import CartItems
from common.models import BaseModel

"""
Order model:
- customer: ForeignKey to profile
- cart_items: ManyToManyField to CartItem
- status: CharField with choices
- total_price: DecimalField
- created_at: DateTimeField
- updated_at: DateTimeField
"""


class OrderStatus(models.TextChoices):
    ACTIVE = "ACTIVE"  # Faol
    PAID = "PAID"  # To'landi
    PROCESSING = "PROCESSING"  # Ishlanmoqda (jarayonda)
    DELIVERED = "DELIVERED"  # Yetkazib berildi
    COMPLETED = "COMPLETED"  # Yakunlandi (mijoz quliga oldi)
    CANCELLED = "CANCELLED"  # Bekor qilindi


class Order(BaseModel):
    customer = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="orders"
    )
    cart_items = models.ManyToManyField(CartItems, related_name="orders")
    status = models.CharField(
        max_length=20, choices=OrderStatus.choices, default=OrderStatus.ACTIVE
    )

    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.customer} - {self.total_price}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"
