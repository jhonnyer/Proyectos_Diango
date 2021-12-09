from django.urls import path

# importas las vists de la app 
from servicios import views
#Importamos las rutas de las imagens que seran vistas en el navegador, del archivo settings
from django.conf import settings
# #Para cargar rutas de archivos estaticos
from django.conf.urls.static import static

urlpatterns = [
    #Creamos las rutas de las vistas
    path('',views.servicios, name='Servicios'),
]
