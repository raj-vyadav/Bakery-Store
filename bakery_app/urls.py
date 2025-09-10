# bakery_app/urls.py
from rest_framework import routers
from .views import CategoryViewSet, ProductViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = router.urls

