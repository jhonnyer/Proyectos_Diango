"""TiendaOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# Importo las vistas 
from gestionPededidos import views
from gestionPededidos.forms import formView_prueba,AuthorCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('busqueda_productos/',views.busqueda_productos),
    path('buscar/',views.buscar),
    path('contacto/',views.contacto),
    path('peliculas/',views.ContactFormView.as_view()),
    path('gracias/',views.gracias),
    path('categoria/',formView_prueba.as_view()),
    # path('prueba_form/',views.contacto_prueba),
    path('cliente/',AuthorCreateView.as_view()),
]
