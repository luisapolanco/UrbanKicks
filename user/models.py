from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length=10)
    is_customer = models.BooleanField(default=False) 
    is_adm = models.BooleanField(default=False)
    old_cart = models.CharField(max_length=200, blank=True, null=True)

    @property
    def is_Customer(self):
        return self.is_customer
    
    @property
    def is_Adm(self):
        return self.is_adm

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='Cliente')
    payment_info = models.CharField(max_length=100)
    customer_id = models.IntegerField()

    def __str__(self):
        return self.customer_id

class Adm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='Adm', default='')
    adm_id = models.IntegerField()

    def __str__(self):
        return self.adm_id