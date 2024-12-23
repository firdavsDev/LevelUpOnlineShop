from django.contrib import messages  # for send messages to frontend
from django.db import transaction
from django.shortcuts import redirect, render

from cart.models import Cart
from cart.utils import get_session_key

from ..models import CustomUser
from ..forms import RegistarForm


@transaction.atomic  # bitta ish bajarilmasa boshqa ishlar ham bajarilmasin
def register(request):
    try:
        registar_form = RegistarForm()
        if request.method == "POST":
            registar_form = RegistarForm(data=request.POST)
            if registar_form.is_valid():
                user_obj = registar_form.save()

                session_key = get_session_key(request)
                cart_obj, _ = Cart.objects.get_or_create(session_key=session_key)
                cart_obj.user = user_obj
                cart_obj.save()
                messages.success(request, "Account created successfully")
                context = {
                    "registar_form":registar_form,
                }
                return redirect("login")
        context = {
            "registar_form":registar_form,
        }
        return render(request, "accounts/register.html", context)
    except Exception as e:
        messages.error(request, f"Error creating account: {e}")
        return redirect("register")
