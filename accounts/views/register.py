from django.contrib import messages  # for send messages to frontend
from django.db import transaction
from django.shortcuts import redirect, render

from cart.utils import get_user_cart

from ..forms import RegistarForm


@transaction.atomic  # bitta ish bajarilmasa boshqa ishlar ham bajarilmasin
def register(request):
    try:
        registar_form = RegistarForm()
        if request.method == "POST":
            registar_form = RegistarForm(data=request.POST)
            if registar_form.is_valid():
                registar_form.save()
                # callig get_user_cart function from cart/utils.py
                get_user_cart(request)
                messages.success(
                    request,
                    "Account created successfully, please check your email to verify your account",
                )
                return redirect("login")
        context = {
            "registar_form": registar_form,
        }
        return render(request, "accounts/register.html", context)
    except Exception as e:
        messages.error(request, f"Error creating account: {e}")
        return redirect("register")
