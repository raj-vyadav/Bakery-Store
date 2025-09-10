from rest_framework import serializers
from .models import Category, Product, Order, CartItem

class ProductSerializer(serializers.ModelSerializer):
   class Meta:
      model = Product
      fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
   products = ProductSerializer(many=True, read_only=True)
   class Meta:
      model = Category
      fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
   class Meta:
      model = Order
      fields = "__all__"


class CartItemSerializer(serializers.ModelSerializer):
   product_name = serializers.CharField(source="product.name", read_only = True)
   product_price = serializers.DecimalField(source="product.price", max_digits=10, decimal_places=2, read_only=True)

   class Meta:
      model = CartItem
      fields = ["id", "product", "product_name", "product_price", "quantity"]