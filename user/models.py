from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    is_cliente = models.BooleanField(default=False) 
    is_adm = models.BooleanField(default=False) # Persona encargada de agregar productos

    @property
    def is_Cliente(self):
        return self.is_cliente
    
    @property
    def is_Adm(self):
        return self.is_adm

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='Cliente')
    Nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.Nombre

class Adm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='Adm', default='')
    Nombre_Empresa = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.Nombre_Empresa