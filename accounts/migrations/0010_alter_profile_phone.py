# Generated by Django 4.2.16 on 2024-12-23 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0009_alter_profile_district"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="phone",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]