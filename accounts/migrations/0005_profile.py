# Generated by Django 4.2.16 on 2024-12-11 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0001_initial"),
        ("accounts", "0004_alter_customuser_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("first_name", models.CharField(max_length=150)),
                ("last_name", models.CharField(max_length=150)),
                ("address", models.TextField()),
                ("phone", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="profile/"),
                ),
                (
                    "district",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="district",
                        to="common.district",
                    ),
                ),
                (
                    "region",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="region",
                        to="common.region",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Profile",
                "verbose_name_plural": "Profiles",
            },
        ),
    ]