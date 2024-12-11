import random
import string

from django.conf import settings
from .models import Cart


def create_custom_session_key(request):
    "create custom session key randomly"
    session_key = "".join(random.choices(string.ascii_lowercase + string.digits, k=40))
    request.session[settings.CUSTOM_SESSION_KEY] = session_key
    request.session.modified = True
    return session_key


def get_session_key(request):
    session_key = request.session.get(settings.CUSTOM_SESSION_KEY)
    if not session_key:
        print("session_key not found")
        session_key = create_custom_session_key(request)
    return session_key


def get_user_cart(request):
    if request.user.is_authenticated:
        user_cart = Cart.objects.get(user=request.user)
    else:
        session_key = get_session_key(request)
        user_cart, _ = Cart.objects.get_or_create(session_key=session_key)
    return user_cart
