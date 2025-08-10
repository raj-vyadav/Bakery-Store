from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
   name = models.CharField(max_length=50)
   
   def __str__(self):
      return self.name

class Product(models.Model):
   category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
   name = models.CharField(max_length=100)
   description = models.TextField(blank=True)
   price = models.DecimalField(max_digits=6, decimal_places=2)
   available = models.BooleanField(default=True)

   def __str__(self):
      return self.name
   
class Order(models.Model):
   customer_name = models.CharField(max_length=100)
   customer_email = models.EmailField()
   created_at = models.DateTimeField(auto_now_add=True)
   products = models.ManyToManyField(Product)

   def __str__(self):
      return f"Order #{self.id} by {self.customer_name}"