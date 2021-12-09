from django.db import models

# Create your models here.
class Cliente(models.Model):
    #blank indica que los campos no pueden estar vacios
    #default le indicamos un valor por defecto
    #unique en el campo email indica que no pueden existir dos registros con el mismo email
    nombre=models.CharField(max_length=30,  blank=False, default='nulo') 
    direccion=models.CharField(max_length=50,  blank=False, default='nulo')
    email=models.EmailField(max_length=30, unique=True,  blank=False, default='nulo')
    telefono=models.CharField(max_length=10,  blank=False, default='nulo')
    password=models.CharField(max_length=15, blank=False, default='nulo')

class Articulo(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

    # def __str__(self):
    #     return 'Articulo: %s, Precio: %s, Seccion: %s' %(self.nombre,self.precio,self.seccion)

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()


# class Operacion():
#     def __init__(self, digito1, digito2):
#         self.numero1=digito1
#         self.numero2=digito2
    
#     def suma(self):
#         resul=self.numero1+self.numero2
#         return resul
    
#     def resta(self):
#         resul=self.numero1-self.numero2
#         return resul
    
#     def multiplicacion(self):
#         resul=self.numero1*self.numero2
#         return resul
    
#     def division(self):
#         resul=self.numero1/self.numero2
#         return resul
    
# objeto=Operacion(5,2)
# resultado=objeto.suma()
# print("El resultado del metodo es: %s"%resultado)
