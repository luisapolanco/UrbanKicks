from django.db import models
from user.models import Customer

# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    products = models.CharField(max_length=200)

    def __str__(self):
        return self.order_id