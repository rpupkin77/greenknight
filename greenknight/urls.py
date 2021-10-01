from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProductViewSet, CategoryViewSet, SupplierViewSet, CartItemViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'suppliers', SupplierViewSet, basename="supplier")
router.register(r'categories', CategoryViewSet, basename="category")
router.register(r'products', ProductViewSet, basename="product")
router.register(r'cart-items', CartItemViewSet, basename="cart-items")

urlpatterns = [path('', include(router.urls))]
