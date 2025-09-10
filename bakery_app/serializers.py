# store/serializers.py

from rest_framework import serializers
from .models import Category, Product, CartItem, Order, OrderItem
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
   class Meta:
      model = Product
      fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
   products = ProductSerializer(many=True, read_only=True)
   class Meta:
      model = Category
      fields = ['id', 'name', 'products']

class CartItemSerializer(serializers.ModelSerializer):
   product_name = serializers.CharField(source="product.name", read_only=True)
   product_price = serializers.DecimalField(source="product.price", max_digits=10, decimal_places=2, read_only=True)
   total_price = serializers.ReadOnlyField()

   class Meta:
      model = CartItem
      fields = ["id", "product", "product_name", "product_price", "quantity", "total_price"]

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at', 'is_paid', 'total_amount', 'items']

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, label='Confirm Password', style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user