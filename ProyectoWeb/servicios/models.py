from django.db import models

# Create your models here.
class Servicio(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    # upload_to='servicios' indica donde se van a subir los archivos media de la app de servicios dentro de la carpeta media 
    imagen=models.ImageField(upload_to='servicios')
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)
    # Nombre del servicio que tendra en la base de datos 
    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'

    def __str__(self):
        return self.titulo


        