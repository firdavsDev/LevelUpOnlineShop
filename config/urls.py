from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from config.views import hello_func, home_page

# hamma url shu yerda yoziladi
urlpatterns = [
    path("admin/", admin.site.urls),
    # cusom urls
    path("hello/", hello_func),
    path("home_page/", home_page),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
