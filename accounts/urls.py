from django.urls import path

from .views import login_form, logout_view, register

urlpatterns = [
    path("login/", login_form, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout_view, name="logout"),
]
