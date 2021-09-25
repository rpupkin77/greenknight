from .models import Product, Supplier, ProductCategory
from .serializers import ProductSerializer, SupplierSerializer, ProductCategorySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class ProductList(APIView):

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SupplierList(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    def list(self, request):
        queryset = Supplier.objects.all()
        serializer = SupplierSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Supplier.objects.all()
        supplier = get_object_or_404(queryset, pk=pk)
        serializer = SupplierSerializer(supplier)
        return Response(serializer.data)

    def destroy(self, request, pk):

        queryset = Supplier.objects.all()
        supplier = get_object_or_404(queryset, pk=pk)
        supplier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request, pk=None):

        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)

            return Response({serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryList(viewsets.ModelViewSet):

    queryset = ProductCategory.objects.all().order_by('name')
    serializer_class = ProductCategorySerializer
    #permission_classes = [permissions.IsAuthenticated]
