from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    brand = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    #images = models.ForeignKey('ImageModel', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Stock(models.Model):

    stock_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'Stock ID: {self.stockid}, Product ID: {self.productid}, Quantity: {self.quantity}'
    