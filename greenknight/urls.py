from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProductList, SupplierList, CategoryList
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'suppliers', SupplierList)


urlpatterns = [
    path('products/', ProductList.as_view()),
    path('categories/', CategoryList.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns.append(path('', include(router.urls)))