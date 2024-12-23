# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from smart_selects.db_fields import ChainedForeignKey

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
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)  # unique=True
    image = models.ImageField(
        upload_to="profile/", null=True, blank=True, default="profile/avatar.jpg"
    )
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    birth_date = models.DateField(null=True)
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name="region", null=True
    )
    # district = models.ForeignKey(
    #     District, on_delete=models.CASCADE, related_name="district", null=True
    # )
    district = ChainedForeignKey(
        District,
        chained_field="region",  # this model field
        chained_model_field="region",  # District model field
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True,
    )
    address = models.TextField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        self.first_name = self.user.first_name
        self.last_name = self.user.last_name
        self.email = self.user.email
        self.phone = self.user.phone
        super(Profile, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
