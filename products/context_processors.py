from cart.models import Cart, CartItems
from products.models import Category


def custom_data(request):
    # 1) Bu context_processors ni ishlatish uchun settings.py faylida context_processors qismiga qo'shish kerak
    categories = Category.objects.filter(is_active=True)
    cart_items_count = 0
    if request.user.is_authenticated:
        user_cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items_count = CartItems.objects.filter(cart=user_cart).count()
    return {"categories": categories, "cart_items_count": cart_items_count}
