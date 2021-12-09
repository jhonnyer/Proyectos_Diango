"""Proyecto1 URL Configuration

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
# Ver procesos de django y matarlo 
# ps auxw | grep runserver

from Proyecto1.views import calculaEdad, calculaEdades, dameFecha, despedida, loader_plantilla, loader_short_plantilla, musica, saludo, curso_django, curso_css, tareas, tareasprueba, games, musica, tecnologias
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/',saludo),
    path('despedida/',despedida),
    path('fecha/',dameFecha),
    path('edades/<int:agno>',calculaEdad),
    path('edad/<int:edad>/<int:agno>',calculaEdades),
    path('plantillas/',loader_plantilla),
    path('plantilla/',loader_short_plantilla),
    path('curso_django/',curso_django),
    path('curso_css/',curso_css),
    path('tareas/',tareas),
    path('tareasprueba/<int:a>/<int:b>',tareasprueba),
    path('games/',games),
    path('musica/',musica),
    path('tecnologias/',tecnologias)
]
