from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProductList, SupplierList

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('suppliers/', SupplierList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)