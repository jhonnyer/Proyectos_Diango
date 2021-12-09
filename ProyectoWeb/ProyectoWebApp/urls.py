from django.urls import path

# importas las vists de la app 
from ProyectoWebApp import views
#Importamos las rutas de las imagens que seran vistas en el navegador, del archivo settings
from django.conf import settings
# #Para cargar rutas de archivos estaticos
from django.conf.urls.static import static

urlpatterns = [
    #Creamos las rutas de las vistas
    path('',views.home, name='Home'),
    path('tienda',views.tienda, name='Tienda'),
    path('blog',views.blog, name='Blog'),
    path('contacto',views.contacto, name='Contacto'),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)