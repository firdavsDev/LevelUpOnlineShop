from django.contrib import messages  # for send messages to frontend
from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import redirect, render

from cart.utils import get_session_key, save_user_cart_items

from ..forms import SimpleLoginForm


def login_form(request):
    if request.method == "POST":
        form = SimpleLoginForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            session_key = get_session_key(request)
            user = authenticate(email=user_email, password=password)
            if user is not None:
                auth_login(request, user)
                # TODO after anymous user login, save cart items to existing user cart
                # save_user_cart_items(user, session_key)
                messages.success(request, "Logged in successfully")
                return redirect("home")
            else:
                messages.error(request, "Login or password is incorrect")
                return redirect("login")
    else:
        form = SimpleLoginForm()

    context = {
        "form": form,
    }
    return render(request, "accounts/login_form.html", context)


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("login")
