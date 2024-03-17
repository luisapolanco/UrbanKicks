from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_lenght = 100)
    city = models.CharField(max_lenght = 100)
    address = models.CharField(max_lenght = 100)
    phone_number = models.CharField(max_lenght=10)
    is_cliente = models.BooleanField(default=False) 
    is_adm = models.BooleanField(default=False) # Persona encargada de agregar productos

    @property
    def is_Cliente(self):
        return self.is_cliente
    
    @property
    def is_Adm(self):
        return self.is_adm

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='Cliente')
    payment_info = models.CharField(max_length=100)
    customer_id = models.IntegerField(max_length = 10)

    def __str__(self):
        return self.customer_id

class Adm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='Adm', default='')
    adm_id = models.IntegerField(max_length = 10)

    def __str__(self):
        return self.adm_id