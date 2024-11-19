from django.db import models

"""
Products Fields:
- name: CharField
- price: DecimalField
- description: TextField
- images (many-to-many): ImageField
- category (many-to-one): ForeignKey
- size (many-to-many): CharField
- color (many-to-many): CharField
- stock: IntegerField
- is_active: BooleanField
- created_at: DateTimeField
"""


class Category(models.Model):
    name = models.CharField(max_length=255)
    # common fields
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Maxsulot nomi")
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 999999.99
    description = models.TextField(
        help_text="Maxsulotni maqtab yoz"
    )  # unlimited length
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField()
    # common fields
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
