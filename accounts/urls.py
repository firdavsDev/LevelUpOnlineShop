from django.urls import path

from .views import login_form, logout_view, profile, register

urlpatterns = [
    path("login/", login_form, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile, name="profile"),
]
