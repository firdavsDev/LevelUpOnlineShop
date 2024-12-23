from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from common.email_verifycation import send_verification_email

from .models import CustomUser


@receiver(post_save, sender=CustomUser)
def send_email_code(sender, instance, created, **kwargs):
    if created:
        # send email verification
        send_verification_email(instance.id, instance.email)
