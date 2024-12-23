from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import redirect

from accounts.models import CustomUser, Profile
from common.email_verifycation import verify_email_code


def verify_email(request, email_code):
    try:
        user_id = verify_email_code(email_code)
        user = CustomUser.objects.get(id=user_id)
        user.is_active = True
        user.save()
        # create profile
        Profile.objects.get_or_create(user=user)
        messages.success(request, "Email tasdiqlandi, iltimos login qiling")
        return redirect("login")
    except Exception as e:
        messages.error(request, f"Xatolik yuz berdi: {e}")
        return redirect("register")
