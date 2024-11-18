from django.contrib import messages  # for send messages to frontend
from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import redirect, render

from .forms import SimpleLoginForm
from .models import CustomUser


def login_view(request):
    if request.method == "POST":
        form = SimpleLoginForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=user_email, password=password)
            if user is not None:
                auth_login(request, user)
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


# def login(request):
#     if request.method == "POST":
#         user_email = request.POST.get("email")
#         password = request.POST.get("password")

#         user = authenticate(email=user_email, password=password)
#         if user is not None:
#             auth_login(request, user)
#             messages.success(request, "Logged in successfully")
#             return redirect("home")
#         else:
#             messages.error(request, "Login or password is incorrect")
#             return redirect("login")
#     return render(request, "accounts/login.html")


def register(request):
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

        user_obj = CustomUser.objects.create(
            first_name=f_name,
            last_name=l_name,
            email=user_email,
            password=password1,
        )
        print(user_obj.email)
        messages.success(request, "Account created successfully")
        return redirect("login")

    return render(request, "accounts/register.html")


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("login")
