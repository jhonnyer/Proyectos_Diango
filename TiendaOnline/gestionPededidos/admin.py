from django.contrib import admin

#Modelos importados de las tablas a modificar
from gestionPededidos.models import Cliente, Articulo, Pedidos

#clase clientesAdmin que va a heredar en la calase admin
#Permite definir que campos quiero que se miren en el panel de administracion
class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","telefono",'email')
    #Añadir casilla de busqueda en el panel de administracion de clientes
    search_fields=('nombre','telefono')

#Clase creada para filtrar por seccion en articulos
class ArticulosAdmin(admin.ModelAdmin):
    list_display=("nombre","seccion","precio")
    #se agrega una tupla para especificar que se va a filtrar, por eso se coloca una tupla
    list_filter=('seccion',)
    search_fields=('nombre','precio')

#Filtrar tabla pedidos por fecha
class PedidosAdmin(admin.ModelAdmin):
    list_display=('numero','fecha','entregado')
    list_filter=('fecha','entregado')
    #añadir campo de filtro de fecha por meses en un menu horizontal
    date_hierarchy='fecha'

# Register your models here.
#registramos los modelos
# admin.site.register(Cliente, ClientesAdmin) #Se registra la clase creada en clientes
# admin.site.register(Articulo, ArticulosAdmin)
# admin.site.register(Pedidos,PedidosAdmin)

admin.site.register(Cliente, ClientesAdmin) #Se registra la clase creada en clientes
admin.site.register(Articulo, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)