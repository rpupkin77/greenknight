from ..models import Supplier
from ..serializers import SupplierSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class SupplierViewSet(viewsets.ModelViewSet):
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
        return Response({"status": "deleted", "id": pk}, status=status.HTTP_204_NO_CONTENT)

    def create(self, request, pk=None):

        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)

            return Response({"id": serializer.data['id'], "status": "created", "name": serializer.data['name']},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):

        queryset = Supplier.objects.all()
        supplier = get_object_or_404(queryset, pk=pk)
        serializer = SupplierSerializer(supplier, data=request.data, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)

            return Response({"id": serializer.data['id'], "name": serializer.data['name'],
                             "status": "updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


