import django
from django.db import models
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls.exceptions import NoReverseMatch
from django.views.generic.base import TemplateView
from gestor.models import Articulo, Cliente
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.
def formularioBusqueda(request):
    arti=[]
    ar=Articulo.objects.all()
    for i in ar:
        arti.append(i.seccion)
    arti=sorted(list(set(arti)))
    return render(request,'formBusqueda.html', {'articulos':arti})


# def resultado(request):
#     encontro=True
#     #Primer busqueda va ser por nombre y seccion indicada en el formulario

#     bubsqueda=request.GET['producto']
#     resultado=Articulo.objects.filter(nombre=bubsqueda)
#     mensaje=" "
#     # mensaje="El resultado es: %s" %resultado[0]
#     for i in resultado:
#         mensaje="%s Nombre: %s, Seccion=%s, Precio=%s" %(mensaje, i.nombre, i.seccion, i.precio)
#     return HttpResponse(mensaje)


def resultado(request):
    # Condicional encargado de verificar el numero de caracteres de la entrada de datos del filtro por nombre en el formulario de busqueda 
    if len(request.GET['producto'])>=20:
        arti=[]
        ar=Articulo.objects.all()
        for i in ar:
            arti.append(i.seccion)
        arti=sorted(list(set(arti)))
        return render(request, 'formBusqueda.html',{'articulos':arti, 'error':True})
    # Filtro para comprobar busqueda de un elemento 
    encontrado=True
     #Primer busqueda va ser por nombre y seccion indicada en el formulario
    if not(request.GET['producto']=='') and not (request.GET['seccion']=='todos'):
        nombre=request.GET['producto']
        seccion=request.GET['seccion']
        resultado=Articulo.objects.filter(nombre__icontains=nombre, seccion=seccion)
     #Busqueda por nombre del producto unicamente y todas las secciones
    elif not(request.GET['producto']=='') and request.GET['seccion']=='todos':
        nombre=request.GET['producto']
        resultado=Articulo.objects.filter(nombre__icontains=nombre)
    #Busqueda por secciones, no introdujo nada en el nombre del producto
    elif (request.GET['producto']=='') and not request.GET['seccion']=='todos':
        seccion=request.GET['seccion']
        resultado=Articulo.objects.filter(seccion=seccion)
    #Busqueda donde el usuario no introduce ni nombre del articulo y deja la lista desplegable igual a todos
     #mostrar toda la informacion
    elif (request.GET['producto']=='') and request.GET['seccion']=='todos':
        resultado=Articulo.objects.all()
    #Si no encontro resultados en la base de datos, se coloca encontro igual a false
    #Encontro se le conoce como bandera de control 
    if not resultado:
        encontrado=False

    return render(request, 'resultado.html',{'registro':resultado, 'status':encontrado})

def registro(request):
    return render(request,'registro.html')

def validacion(request):
    nombre=request.POST['nombre']
    direccion=request.POST['direccion']
    telefono=request.POST['telefono']
    email=request.POST['email']
    password=request.POST['password']
    passwordRep=request.POST['passwordRep']
    # validacion errores de datos provenientes del formulario en la funcion verificacion
    status=verificacion(nombre, direccion, telefono, password, passwordRep, email)

    #verificamos que no hayan habido errores en la validación del formulario mediante el diccionario que devulve la funcion verificacion
    #verificamos que no haya habido almenos una llave en el diccionario
    if len(list(status.keys()))>0:
        return render(request,'registro.html',{'status':status})
    else:
        Cliente.objects.create(nombre=nombre,direccion=direccion,email=email,telefono=telefono,password=password)
        return render(request,'registroExitoso.html',{'nombre':nombre})

def verificacion(nombre,direccion,telefono,password,passwordRep,email):
    dicError={}
    if len(nombre)>=40 or len(nombre)<3:
        dicError.setdefault('errorNombre',"El nombre debe contener mas de 3 letras y menor o igual a 40 letras ")
    
    if not(len(telefono)==10):
        dicError.setdefault('errorTelefono',"El número telefonico debe tener 10 digitos númericos")
    for i in telefono:
        if ord(i) <48 or ord(i)>58:
            if 'errorTelefono' in dicError:
                dicError['errorTelefono']='El telefono solo puede contener numeros'
                break
            else:
                dicError.setdefault('errorTelefono',"El número telefonico no puede contener letras")
    

    if len(direccion)==0:
        dicError.setdefault('errorDireccion',"Debe ingresar una dirección")
    
    if len(password)>=21 or len(password)<=7:
        if 'errorPassword' in dicError:
            dicError['errorPassword']= "La contraseña debe contener mas de 8 caracteres y menos de 21"
        else:
            dicError.setdefault('errorPassword',"La contraseña debe contener mas de 8 caracteres y menos de 21")
    
    if not(password==passwordRep):
        if 'errorPassword' in dicError:
            dicError['errorPassword']="Las contraseñas ingresadas no coinciden, por favor verificar"
        else:
            dicError.setdefault('errorPassword',"Las contraseñas ingresadas no coinciden, por favor verificar")
    
    if len(email)==0:
        dicError.setdefault('errorEmail','Debe ingresar un correo')
    emailBase=Cliente.objects.filter(email=email)
    if not len(emailBase)==0:
        if 'errorEmail' in dicError:
            dicError['errorEmail']="El correo electronico no esta disponible, por favor utilice otro"
        else:
            dicError.setdefault('errorEmail',"El correo electronico no esta disponible, por favor utilice otro")
    
    return dicError

class ContactFormView(FormView):
    template_name = 'contacto.html'
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


class ClientesDetalles(DetailView):
    model=Cliente
    template_name='articuloDetalle.html'
    # override context data
    def get_context_data(self, *args, **kwargs):
        context = super(ClientesDetalles,
             self).get_context_data(*args, **kwargs)
        # add extra field 
        context["category"] = "MISC"        
        return context

class ClientesLista(ListView):
    model=Cliente
    template_name='ListaClientes.html'