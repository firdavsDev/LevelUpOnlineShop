from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from config.views import home_page

# hamma url shu yerda yoziladi
urlpatterns = [
    path("", home_page, name="home"),
    path("admin/", admin.site.urls),
    # Smart Selects URLs
    path("chaining/", include("smart_selects.urls")),
    # Accounts App URLs
    path("accounts/", include("accounts.urls")),
    # Products App URLs
    path("products/", include("products.urls")),
    # Cart apps
    path("cart/", include("cart.urls")),
    # Order apps URLs
    path("order/", include("order.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
