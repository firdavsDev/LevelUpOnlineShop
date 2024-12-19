from django.contrib import messages  # for send messages to frontend
from django.db import transaction
from django.shortcuts import redirect, render

from cart.models import Cart
from cart.utils import get_session_key

from ..models import CustomUser


@transaction.atomic  # bitta ish bajarilmasa boshqa ishlar ham bajarilmasin
def register(request):
    try:
        if request.method == "POST":
            f_name = request.POST.get("f_name")
            l_name = request.POST.get("l_name")
            user_email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")

            if password1 != password2:
                messages.error(request, "Passwords do not match")
                return redirect("register")

            # check if email already exists
            user = CustomUser.objects.filter(email=user_email)
            if user:
                messages.error(request, "Email is already taken")
                return redirect("register")

            user_obj = CustomUser.objects.create_user(
                email=user_email,
                password=password1,
                username=user_email,
                first_name=f_name,
                last_name=l_name,
                is_active=False,  # if user verified email, then is_active=True
            )
            # create cart for user (request)
            session_key = get_session_key(request)
            cart_obj, _ = Cart.objects.get_or_create(session_key=session_key)
            cart_obj.user = user_obj
            cart_obj.save()
            messages.success(request, "Account created successfully")
            return redirect("login")

        return render(request, "accounts/register.html")
    except Exception as e:
        messages.error(request, f"Error creating account: {e}")
        return redirect("register")
