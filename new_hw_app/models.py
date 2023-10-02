from django.utils import timezone
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    registration_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, age: {self.age}'

    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/')
    registration_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'Product: {self.name}, price: {self.price}, description: {self.description}'
    
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f' Order: {self.customer}, products: {self.products}, total_price: {self.total_price}'