# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel, District, Region

from .manager import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone"]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = _("CustomUser")
        verbose_name_plural = _("CustomUsers")


class Profile(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="profile/", null=True, blank=True, default="profile/avatar.jpg"
    )
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    birth_date = models.DateField()
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name="region", null=True
    )
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name="district", null=True
    )
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
