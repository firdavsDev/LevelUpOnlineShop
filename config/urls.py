from django.contrib import admin
from django.urls import path

from config.views import hello

# hamma url shu yerda yoziladi
urlpatterns = [
    path("admin/", admin.site.urls),
    # /hello url - Salom dunyo sozini chiqaradi
    path("hello/", hello),
]
