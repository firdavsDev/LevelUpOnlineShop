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


# TODO move to common app
class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Bu classni bazada table yaratmasin


class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Kategoriyalar"
        verbose_name = "Kategoriya"


class Product(BaseModel):
    name = models.CharField(
        max_length=255, verbose_name="Maxsulot nomi"
    )  # 'id' is auto created and hidden field
    image = models.ImageField(
        upload_to="products", help_text="Maxsulot rasmi", null=True
    )  # upload_to="products" -> media/products folder
    description = models.TextField(
        help_text="Maxsulotni maqtab yoz"
    )  # unlimited length
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Maxsulotlar"  # admin panel uchun
        verbose_name = "Maxsulot"
        ordering = ["-created_at"]  # descending order


# null=True - Bu field bo'sh bo'lishi mumkin (database da NULL)
# blank=True - Bu field formda bo'sh bo'lishi mumkin (formda required=False)


class ProductIMG(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )  # if product deleted, all images will be deleted(cascade)
    image = models.ImageField(upload_to="products", help_text="Maxsulot rasmi")

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name_plural = "Maxsulot rasmlari"
        verbose_name = "Maxsulot rasmi"


class Color(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    # TODO meta class


class Size(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    # TODO meta class


class ProductVariation(BaseModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="Maxsulot_nomi",
    )
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name="Rangi")
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="Olchami")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.color.name} - {self.size.name}"

    class Meta:
        verbose_name_plural = "Maxsulot variantlari"
        verbose_name = "Maxsulot varianti"
        unique_together = [
            "product",
            "color",
            "size",
        ]  # unique together bu fieldlarni birgalikda bazada takrorlanmasligini ta'minlaydi
