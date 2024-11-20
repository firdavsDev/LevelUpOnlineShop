from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from config.views import home_page

# hamma url shu yerda yoziladi
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_page, name="home"),
    # Accounts App URLs
    path("accounts/", include("accounts.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
