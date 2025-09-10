# store/models.py

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
   name = models.CharField(max_length=50, unique=True)

   def __str__(self):
      return self.name

   class Meta:
      verbose_name_plural = "Categories"

class Product(models.Model):
   p_img = models.ImageField(upload_to="products/", null=True, blank=True)
   category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
   name = models.CharField(max_length=100)
   description = models.TextField(blank=True)
   price = models.DecimalField(max_digits=10, decimal_places=2)
   available = models.BooleanField(default=True)

   def __str__(self):
      return self.name

class CartItem(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart_items")
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   quantity = models.PositiveIntegerField(default=1)

   def __str__(self):
      return f"{self.quantity} x {self.product.name} for {self.user.username}"
   
   @property
   def total_price(self):
      return self.quantity * self.product.price

   class Meta:
      unique_together = ('user', 'product')

# store/models.py

class Order(models.Model):
   # Add null=True and blank=True to the user field
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders", null=True, blank=True)
   created_at = models.DateTimeField(auto_now_add=True)
   is_paid = models.BooleanField(default=False)
   total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

   def __str__(self):
      # It's good practice to handle the case where the user might be None
      if self.user:
          return f"Order #{self.id} by {self.user.username}"
      return f"Guest Order #{self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2) # Price at the time of order

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order #{self.order.id}"