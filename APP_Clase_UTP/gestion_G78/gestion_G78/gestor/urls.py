from django.urls import path
from django.urls.resolvers import URLPattern
from gestor.views import formularioBusqueda, resultado, validacion, registro, ContactFormView,ClientesDetalles, ClientesLista

urlpatterns=[
    path('busqueda_producto/',formularioBusqueda),
    path('resultado/',resultado),
    path('registro/',registro),
    path('validacion/',validacion),
    path('contacto/',ContactFormView.as_view()),
    path('<int:pk>/',ClientesDetalles.as_view()),
    path('clientes/',ClientesLista.as_view())
]