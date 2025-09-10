from django.contrib import admin
from django.urls import path, include
from bakery_app.views import home
from django.conf.urls.static import static
from .import settings
from bakery_app.views import AddToCartView, CartView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('bakery_app.urls')),
    path('', home, name='home'),
    path("api/cart/add/", AddToCartView.as_view(), name="add-to-cart"),  # ✅ new
    path("api/cart/", CartView.as_view(), name="cart"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
