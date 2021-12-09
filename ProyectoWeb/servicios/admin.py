from django.contrib import admin
from .models import Servicio

#Creamos clase que hereda el servicio
class ServicioAmin(admin.ModelAdmin):
    #Colocamos los campos created y update en el panel de administracion para solo lectura
    readonly_fields=('created','update')


# Register your models here.
admin.site.register(Servicio, ServicioAmin)
