from django.forms.widgets import SelectDateWidget
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
#Importamos el formulario en el archivo forms.py
from gestionPededidos.forms import FormularioContacto
#Importo modelo Articulos
from gestionPededidos.models import Articulo, Cliente
#importamos librerias para enviar mensajes
from django.core.mail import send_mail
# importamos libreria de settings de django
from django.conf import settings

from gestionPededidos.form1 import ContactForm
from django.views.generic.edit import FormView

from .forms import formView_prueba

# Create your views here.
def busqueda_productos(request):
    return render(request,'busqueda_productos.html')

def buscar(request):
    #Atributo producto viene desde el formulario del html
    #De la peticion obtenemos lo que el usuario enviado utilizando la peticion GET y el name del input del formulario
    if request.GET['producto']: #Verifica si encuentra algo en la peticion que se esta enviando en el formulario, es decir que no este vacio
        producto=request.GET['producto'] #Guarda el valor almacenado o enviado en el formulario
        #Verificar longitud del texto introducido en el formulario almacenado en la variable producto
        if len(producto)>20:
            mensaje='Texto de busqueda demasiado largo'
        else:
            # icontains sustituye o funciona como like en una consulta sql
            # select * from Articulos like nombre='Valor_variable_consulta'
            # En el campo nombre busca el valor que coincida con la variable de consulta
            articulos=Articulo.objects.filter(nombre__icontains=producto)
            # print(articulos)
            # print(producto)
            #Redirigir a un html que permita visualizar la información
            return render(request,'resultado_busqueda.html',{'articulos':articulos,'query':producto})
            # mensaje='Articulo buscado: %r' %request.GET['producto']
    else:
        mensaje='No has introducido nada'
    #Se devuelve el utilizando el mensaje 
    return HttpResponse(mensaje)


# Formulario contacto creado desde API FORMS en el archivo forms.py 
def contacto(request):
    if request.method=='POST':
        # creamos un objeto del tipo de la clase FormularioContacto 
        miformulario=FormularioContacto(request.POST) #request.POST contiene toda la informacion ingresada por el usuario en el formulario
        #Preguntamos si el formulario es valido, si ha pasado la validacion de los campos
        if miformulario.is_valid():
            #Guardamos la informacion del formulario en la variable infForm, crea un diccionario
            infForm=miformulario.cleaned_data
            print(infForm)
            print(infForm['asunto'])
            print(infForm.get('email'))
            print(infForm.get('email',''))
            #'' va el campo de la direccion de correo configurado en el archivo setting, desde donde se envian los correos
            # infForm.get() permite recuperar informacion del correo del formulario en este caso 
            send_mail(infForm['asunto'],infForm['mensaje'],infForm.get('email',''),['jhonnyerg@unicauca.edu.co'],) 
            return render(request,'gracias.html')
    
    else:
        miformulario=FormularioContacto() #formulario sin datos, vacio
    #Crea la vista del formulario
    return render(request,'formulario_contacto.html',{'form':miformulario})

# Funcion formulario contacto creado manualmente, se comenta porque vamos a crear el formulario desde la clase en forms utilizando
# API FORMS
#Funcion para crear un formulario de contacto
# def contacto(request):
#     #Si se detecta que el formulario envia el metodo post
#     if request.method=='POST':
#         # capturamos la informacion correspondiente al asunto 
#         subject=request.POST['asunto']
#         # capturamos el mensaje y el email de la persona quien envio el formulario
#         message=request.POST['mensaje']+' '+request.POST['email']
#         # capturamos el email donde se va a enviar el correo, configurado en setting
#         email_from=settings.EMAIL_HOST_USER
#         # la direccion donde quiero que lleguen los mensajes del formulario, el destinatario
#         recipient_list=['jhonnyerg@unicauca.edu.co','jhonnyergalindez.ruta1@utp.edu.co']
#         print(subject,message,email_from,recipient_list)
#         #enviamos el email al destinatario
#         send_mail(subject,message,email_from,recipient_list)
#         return render(request,'gracias.html')
#     return render(request,'contacto.html')

class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/gracias/'

    def post(self, request, *args, **kwargs):
        form = ContactForm(data=request.POST)
        if form.is_valid():
            # username=form.cleaned_data['nombre']
            # form.save()
            form = ContactForm()
            nombre=request.POST['nombre']
            direccion=request.POST['direccion']
            email=request.POST['email']
            telefono=request.POST['telefono']
            print(nombre)
            print(email)
            Cliente.objects.create(nombre=nombre,direccion=direccion,email=email,telefono=telefono)
            return render(request, 'gracias.html')
        return render(request, 'gracias.html')


def gracias(request):
    return render(request, 'gracias.html')


# def contacto_prueba(request):
#     if request.method=='GET':
#         form=formView_prueba(request.GET)
#         if form.is_valid():
#             form=formView_prueba()
#             username=request.POST['nombre']
#             return render(request,'gracias.html',{'username':username})
#     return render(request,'gracias.html')