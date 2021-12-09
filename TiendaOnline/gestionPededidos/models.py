from django.db import models
from django.db.models.fields import EmailField

# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=30) #CharField quiere decir que deja introducir texto
    direccion=models.CharField(max_length=50) #Max_length indica la cantidad de caracteres que acepta
    email=EmailField(blank=True,null=True, verbose_name='correo') #El campo se coloca no requerido
    telefono=models.CharField(max_length=10)
    password=models.CharField(max_length=20, default='nulo')
    # def __str__(self):
    #     return self.nombre

class Articulo(models.Model):
    nombre=models.CharField(max_length=30) #CharField quiere decir que deja introducir texto
    seccion=models.CharField(max_length=20) #Max_length indica la cantidad de caracteres que acepta
    precio=models.IntegerField()

    # def __str__(self) -> str:
    #     return 'El nombre es %s, la sección es: %s y el precio es: %s' %(self.nombre,self.seccion,self.precio)

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()
    #Sino hay return devuelve el modelo