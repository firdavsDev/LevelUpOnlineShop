# Generated by Django 4.2.16 on 2024-11-19 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(help_text='Maxsulotni maqtab yoz'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Maxsulot nomi'),
        ),
    ]
