# store/models.py
from django.db import models
from django.contrib.auth.models import User

# 1. Product Model (Website par bikne waale samaan)
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True, null=True) # Abhi ke liye hum image links use karenge
    stock = models.IntegerField(default=10)

    def __str__(self):
        return self.name

# 2. Order Model (User jab kuch khareedega)
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False) # True matlab order process ho gaya
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username if self.user else 'Guest'}"

# 3. OrderItem Model (Ek order ke andar kaun-kaun se products hain)
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"