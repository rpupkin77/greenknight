from django.db import models
from django.contrib.auth.models import User

class base_element(models.Model):
    """
            Base element, abstract class
    """
    name = models.CharField(max_length=128)
    short_description = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField(db_index=True, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Supplier(base_element):
    """
        Supplier - can have many products
    """
    url = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    address_one = models.CharField(max_length=256, blank=True, null=True)
    address_two = models.CharField(max_length=256, blank=True, null=True)
    city = models.CharField(max_length=128, blank=True, null=True)
    state_province = models.CharField(max_length=128, blank=True, null=True)
    country = models.CharField(max_length=128, blank=True, null=True)
    postal_code = models.CharField(max_length=32, blank=True, null=True)
    discount_percent = models.IntegerField(default=0, help_text="Will be applied to all products by this" \
                                                                              "supplier")

class ProductCategory(base_element):
    """
    Product category - can have itself as a parent
    """
    parent_category = models.ForeignKey("ProductCategory", null=True, on_delete=models.CASCADE)
    discount_percent = models.IntegerField(default=0, help_text="Will be applied to all products in this" \
                                                                              "category")


class Product(base_element):
    """
    Product model
    """
    category = models.ForeignKey(ProductCategory, on_delete=models.RESTRICT, blank=True, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount_percent = models.IntegerField(default=0, blank=True, null=True)
    quantity_available = models.IntegerField(default=1, blank=True, null=True)
    sku = models.CharField(max_length=16, blank=True, null=True)
    digital_only = models.BooleanField(default=False)

class ProductImage(models.Model):
    image = models.ImageField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    alt_text = models.CharField(max_length=128, blank=True, null=True)

class Cart(models.Model):
    """
    Cart model
    """
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=1)





