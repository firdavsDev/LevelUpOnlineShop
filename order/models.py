from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import Profile
from cart.models import CartItems
from common.models import BaseModel, District, Region

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


class Delivery(BaseModel):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="delivery"
    )
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name="delivery_region", null=True
    )
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name="delivery_district", null=True
    )
    street = models.CharField(max_length=100, blank=True, null=True)
    building = models.CharField(max_length=50, blank=True, null=True)
    house = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(_("email address"))
