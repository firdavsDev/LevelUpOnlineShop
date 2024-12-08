from django.db.models.signals import post_save
from django.dispatch import receiver

from cart.models import Cart

from .models import CustomUser


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Cart.objects.get_or_create(user=instance)
        print("User created")
