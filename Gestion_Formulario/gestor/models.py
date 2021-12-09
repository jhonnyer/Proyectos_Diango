from django.db import models

# Create your models here.

class Cliente(models.Model):
    username=models.CharField(max_length=30)
    telefono=models.IntegerField(max_length=10)
    email=models.EmailField(max_length=50)
    direccion=models.CharField(max_length=50)