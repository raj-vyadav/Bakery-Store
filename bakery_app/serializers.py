from rest_framework import serializers
from .models import Category, Product, Order

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

