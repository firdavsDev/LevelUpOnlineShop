from django.urls import path

from .views import login_form, logout_view, profile, register, update_profile

urlpatterns = [
    path("login/", login_form, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile, name="profile"),
    path("update_profile/", update_profile, name="update_profile")
]
