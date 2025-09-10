from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    # API routes
    path('api/', include(router.urls)),
    path('api/cart/', views.CartView.as_view(), name='cart-api'),
    path('api/checkout/', views.CheckoutView.as_view(), name='checkout-api'),
    path('api/orders/', views.OrderHistoryView.as_view(), name='orders-api'),

    # Template-rendered pages
    path('', views.home, name='home'),
    path('cart/', views.cart_page, name='cart-page'),
    path('orders/', views.order_page, name='order-page'),
]
