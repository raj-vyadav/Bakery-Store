from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Product, Order, CartItem
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer, CartItemSerializer
from django.shortcuts import render

class CategoryViewSet(viewsets.ModelViewSet):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
   queryset = Product.objects.all()
   serializer_class = ProductSerializer
   search_fields = ['name', 'description']
   ordering_fields = ['price', 'name']

class OrderViewSet(viewsets.ModelViewSet):
   queryset = Order.objects.all()
   serializer_class = OrderSerializer

def home(request):
   return render(request, 'index.html')

class AddToCartView(APIView):
   def post(self, request):
      user = request.user
      product_id = request.data.get("product_id")
      quantity = int(request.data.get("quantity", 1))

      try:
         product = Product.objects.get(id=product_id)
      except Product.DoesNotExist:
         return Response({"error": "Product not found"}, status = status.HTTP_404_NOT_FOUND)
      
      cart_item, created = CartItem.objects.get_or_create(user=user, product=product)

      if not created:
         cart_item.quantity += quantity
      else:
         cart_item.quantity = quantity
      
      cart_item.save()
      items = CartItem.objects.filter(user=user)

      return Response(
            {
                "message": message,
                "cart": CartItemSerializer(items, many=True).data
            },
            status=status.HTTP_200_OK
        )
      
class CartView(APIView):
    def get(self, request):
        cart_items = CartItem.objects.all()  # later, filter by user
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)