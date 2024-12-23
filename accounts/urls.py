from django.urls import path

from .views import login_form, logout_view, profile, register, update_profile, get_districts_by_region

urlpatterns = [
    path('get-districts/<int:region_id>/', get_districts_by_region, name='get_districts_by_region'),
    path("login/", login_form, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout_view, name="logout"),
    path("profile/", update_profile, name="profile"),
    path("update_profile/", update_profile, name="update_profile"),
    path("get-districts-by-region/<int:region_id>/", get_districts_by_region, name="get_districts_by_region"),
]
