# Generated by Django 4.2.16 on 2024-11-21 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.PositiveIntegerField()),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Rangi', to='products.color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Maxsulot_nomi', to='products.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Olchami', to='products.size')),
            ],
        ),
    ]