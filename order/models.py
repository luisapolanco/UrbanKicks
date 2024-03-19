from django.db import models
from user.models import Customer

# Create your models here.
class Order(models.Model):
    order_id = models.CharField(max_length=50, unique=True,primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart_id = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_shipped = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.order_id