from rest_framework import serializers
from .models import Product, Supplier, ProductCategory, CartItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'short_description', 'category', 'supplier',
                  'sku', 'price', 'discount_percent', 'enabled', 'quantity_available', 'digital_only'
                  ]


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product',  'quantity', 'cart']


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'description', 'short_description', 'parent_category',
                  'discount_percent', 'enabled'
                  ]

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'description', 'short_description', 'address_one', 'address_two', 'city',
                  'state_province', 'country', 'postal_code', 'email', 'url', 'phone', 'discount_percent', 'enabled']