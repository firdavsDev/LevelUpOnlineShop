from django.shortcuts import redirect, render

from .models import Category, Product, ProductIMG


def products(request):
    products = Product.objects.filter(is_active=True)
    categorys = Category.objects.filter(is_active=True)
    product_images = ProductIMG.objects.all()
    return render(
        request,
        "store/products.html",
        context={"products": products, "categorys": categorys, "product_images": product_images},
    )


def product_detail(request, product_id):
    try:
        # product_id bu url dan kelgan qiymat bo'ladi
        product = Product.objects.get(
            id=product_id, is_active=True
        )  # get(field1=value, field_n=value) methodi faqatgina 1 ta qiymat qaytaradi
        product_images = ProductIMG.objects.filter(product=product)
        context = {"product": product, "product_images": product_images}
        return render(request, "store/product-detail.html", context=context)
    except Product.DoesNotExist:
        context = {"product": product, "product_images": product_images}
        return redirect("store", context=context)