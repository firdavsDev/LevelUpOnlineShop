from django.db.models.signals import post_save
from django.dispatch import receiver

from common.generate_email_code import send_verification_email

from .models import CustomUser


@receiver(post_save, sender=CustomUser)
def send_email_code(sender, instance, created, **kwargs):
    if created:
        # send email verification
        if send_verification_email(instance.id, instance.email):
            print("Email sent successfully")
