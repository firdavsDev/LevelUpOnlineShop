from products.models import Category


def custom_data(request):
    # 1) Bu context_processors ni ishlatish uchun settings.py faylida context_processors qismiga qo'shish kerak

    categories = Category.objects.filter(is_active=True)
    return {"categories": categories}
