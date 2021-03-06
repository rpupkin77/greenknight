from rest_framework import serializers
from .models import Product, Supplier


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'short_description', 'category', 'supplier',
                  'sku', 'price', 'discount_percent', 'enabled', 'quantity_available', 'digital_only'
                  ]


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'description', 'short_description', 'address_one', 'address_two', 'city',
                  'state_province', 'country', 'postal_code', 'email', 'url', 'phone', 'discount_percent', 'enabled']