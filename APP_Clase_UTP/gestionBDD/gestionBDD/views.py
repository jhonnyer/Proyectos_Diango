from django.contrib.messages.api import success
from gestionBDD.settings import TEMPLATES
from django.http import HttpResponse
from django.shortcuts import redirect, render
import datetime

# libreria de django para crear formulario 
from django.contrib.auth.forms import UserCreationForm
# importamos el formulario creado en el modelo, este hereda de userCreationForm
from .formularios import UserRegisterForm

#Mensaje para cuando se realice un registro
from django.contrib import messages

# Librerias para login, autenticacion 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate

from gestor.models import Articulo, Cliente

#Formulario de prueba
from .forms import PeliculasForms
from django.views.generic.edit import FormView

#importamos librerias para enviar mensajes
from django.core.mail import send_mail

from .forms import FormularioContacto

def formulario(request):
    return render(request,'form.html')

# def respuesta(request):
#     nombre=request.GET['nombre']
#     mensaje='Hola %s bienvenido al curso de programación web'%(nombre)
#     return HttpResponse(mensaje)


def respuesta(request):
    anioActual=datetime.datetime.now().year
    diaActual=datetime.datetime.now().day
    mesActual=datetime.datetime.now().month
    fechaNacimiento=request.GET['nacimiento']
    # Formato fecha '2021-11-12' 
    # split genera una lista de esta forma (2021,11,12)
    anioNacimiento=int(request.GET['nacimiento'].split('-')[0])
    mesNacimiento=int(request.GET['nacimiento'].split('-')[1])
    diaNacimiento=int(request.GET['nacimiento'].split('-')[2])

    print(fechaNacimiento)
    print(anioNacimiento)
    print(mesNacimiento)
    print(diaNacimiento)
    
    edad=anioActual-anioNacimiento
    if mesNacimiento>mesActual:
        edad-=1
    elif mesActual==mesNacimiento:
        if diaActual<diaNacimiento:
            edad-=1

    nombre=request.GET['nombre']
    genero=request.GET['genero']
    if genero=='M':
        genero='masculino'
    else:
        genero='femenino'

    return render(request,'respu.html',{'nombre':nombre,'edad':edad,'genero':genero})

def formularioBusqueda(request):
    arti=[]
    # recuperamos todos los articulos del modelo en la base de datos
    ar=Articulo.objects.all()
    for i in ar:
        arti.append(i.seccion)
    arti=sorted(list(set(arti)))
    return render(request,'formBusqueda.html',{'articulos':arti})


# def resultado(request):
#     encontrado=True
#     busqueda=request.GET['producto']
#     resultado=Articulo.objects.filter(nombre=busqueda)
#     # mensaje="El resultdo de la busqueda del producto es: %s" %(resultado[0])
#     mensaje=""
#     for i in resultado:
#         mensaje="%s Nombre: %s, Sección: %s, precio: %s" %(mensaje, i.nombre, i.seccion, i.precio)
#     return HttpResponse(mensaje)


def resultado(request):
    # filtro para comprobar longitud de caracteres en una cadena de texto 
    if len(request.GET['producto'])>=20:
        arti=[]
        ar=Articulo.objects.all()
        for i in ar:
            arti.append(i.seccion)
        arti=sorted(list(set(arti)))
        return render(request,'formBusqueda.html',{'articulos':arti,'error':True})

    # Filtro para comprobar busqueda de un elemento 
    encontrado=True
    if not(request.GET['producto']=='') and not (request.GET['seccion']=='todos'):
        nombre=request.GET['producto']
        seccion=request.GET['seccion']
        resultado=Articulo.objects.filter(nombre__icontains=nombre, seccion=seccion)
    elif not(request.GET['producto']=='') and request.GET['seccion']=='todos':
        nombre=request.GET['producto']
        resultado=Articulo.objects.filter(nombre__icontains=nombre)

    elif (request.GET['producto']=='') and not request.GET['seccion']=='todos':
        seccion=request.GET['seccion']
        resultado=Articulo.objects.filter(seccion=seccion)
    
    elif (request.GET['producto']=='') and request.GET['seccion']=='todos':
        resultado=Articulo.objects.all()

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

def verificacion(nombre, direccion, telefono, password, passwordRep, email):
    dicError={} #Diccionario que almacenara los erroes si se encuentran cuando se vaya a enviar el formulario
    if len(nombre)>=40 or len(nombre)<3:
        #si el nombre tiene mas de 40 letras o menos de 3, se crea una tupla en el diccionario con la clave errornombre y el valor fijado en el siguiente mensaje
        #Se utiliza la funcion setdefault para fijar los valores de la tupla en el diccionario 
        dicError.setdefault('errornombre','El nombre debe contener mas de 3 letras y menor o igual a 40 letras')

    #Verificación telefono que contenga 10 digitos
    if not(len(telefono)==10):
        dicError.setdefault('errorTelefono','El número de telefono debe contener 10 digitos')
    #recorre la cadena de texto del telefono tomando cada uno de sus caracteres y por medio de la funcion ord convierte caracteres
    #en su número ASCII y verifica que ninguno de ellos sea menos a 48 ni mayor a 58 que son valores númericos, en caso contrario quiere
    #decir que no son números
    for i in telefono:
        if ord(i)<48 or ord(i)>58:
            #Se verifica si la tupla errorTelefono ya existe en el diccionario de errores, si existe reemplaza su valor, sino crea una nueva tupla
            if 'errorTelefono' in dicError:
                dicError['errorTelefono']='"El telefono debe contener solo números'
                break
            else:
                dicError.setdefault('errorTelefono','El número de telefono no puede contener letras')
                break

    #Validacion de direccion
    if len(direccion)==0:
        dicError.setdefault('errorDireccion','Debe ingrsar una contraseña')

    # Validacion de contraseña 
    # Verificar que se haya ingresado una contraseña y que no contenga mas de 20 caracteres, ni menos de 8.
    if len(password)>=21 or len(password)<=7:
        if 'errorPassword' in dicError:
            dicError['errorPassword']='La contraseña debe tener al menos 8 caracteres y no puede contener mas de 20 caracteres'
        else:
            dicError.setdefault('errorPassword','La contraseña debe tener al menos 8 caracteres y no debe ser mayor a 20 caracteres')
    
    # Validacion que la contraseña y la contraseña repetida sean iguales 
    if not(password==passwordRep):
        if 'errorPassword' in dicError:
            dicError['errorPassword']='La contraseña y la repetición de la contraseña no coinciden'
        else:
            dicError.setdefault('errorPassword','La contraseña y la repetición de la contraseña no coinciden')
    
    #Verificacion del correo, verifica que el campo no este vacio y que no este repetido en la base de datos
    if len(email)==0:
        dicError.setdefault('errorEmail','Debes ingresar un correo electrónico')
    emailBase=Cliente.objects.filter(email=email)
    if not len(emailBase)==0:
        if 'errorEmail' in dicError:
            dicError['errorEmail']='El correo electrónico no esta disponible, por favor ingrese otro correo'
        else:
            dicError.setdefault('errorEmail','El correo electrónico no esta disponible, por favor ingrese otro correo')
    return dicError



#Vamos a crear un formulario desde la libreria form
def register(request):
    # Si existen variables POST, quiere decir que se accedio a la vista al presionar el boton submit del formulario, entonces se crea el 
    # formulario 
    if request.method=='POST':
        # form=UserCreationForm(request.POST)
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            # guardar registro en la base de datos, el metodo UserCreationForm ya cuanto con modelo que conecta a la base de datos 
            form.save()
            messages.success(request,'Usuario %s creado con exito'%username)
            return redirect('home')
    else:
        # form=UserCreationForm()
        form=UserRegisterForm()
    contexto={'formulario':form}
    return render(request,'register.html',contexto)


# Formulario de ingreso 

#Vamos a crear un formulario desde la libreria form
def ingresar(request):
    # Si existen variables POST, quiere decir que se accedio a la vista al presionar el boton submit del formulario, entonces se crea el 
    # formulario 
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            nombreUsuario=form.cleaned_data.get('username')
            contrasena=form.cleaned_data.get('password')
            # Verifica la autenticacion del usuario 
            usuario=authenticate(username=nombreUsuario,password=contrasena)
            if usuario is not None:
                # Login recibe el request y el usuario para generar la seccion 
                login(request,usuario)
                messages.success(request,"Bienvenido %s a la pagina principal del proyecto de programación web"%nombreUsuario)
                return redirect('home')
            else:
                #en caso de que el usuario no se haya logrado autenticar muestra mensaje de error
                messages.error(request,"El usuario o contraseña son incorrectos")
        else:
            #mensaje de error si el formulario no es valido 
            messages.error(request,"El usuario o contraseña son incorrectos")
    else:
        form=AuthenticationForm()
    contexto={'formulario':form}
    return render(request,'login.html',contexto)

def servicios(request):
    return render(request,'servicios.html')

# Pagina principal del sitio 
def home(request):
    return render(request, 'index.html')

# Pagina de cierre de sesion mediante funcion "logout". Se genera un mensaje de cierre de sesion y redirecciona al formulario inicio sesion 
def salir(request):
    logout(request)
    messages.success(request,'Sesión cerrada')
    return redirect('home')

def peliculas(request):
    if request.method=='POST':
        miform=PeliculasForms(request.POST)
        if miform.is_valid():
            infoForm=miform.cleaned_data
            print(infoForm)
            print(infoForm['descripcion'])
            print(infoForm.get('categoria'))
    return render(request,'gracias.html')

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



def registros_db(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            messages.success(request,'Usuario %s creado con exito'%username)
    else:
        form=UserRegisterForm()
    contexto={'formulario':form}
    return render(request,'registrarse.html',contexto)


# def ingreso_login(request):
#     if request.method=='POST':
#         form=AuthenticationForm(request,request.POST)
#         if form.is_valid():
#             nombre=form.cleaned_data.get('username')
#             contrasena=form.cleaned_data.get('password')
#             usuario=authenticate(unsername=nombre,password=contrasena)
#             if usuario is not None:
#                 login(request, usuario)
#                 messages.success(request, 'Bienvenido %s al ingreso de la plataforma web'%nombre)
#                 return redirect('home')
#             else:
#                 messages.error(request,'El usuario o la contraseña son incorrectos')
#         else:
#             messages.error(request,'El usuario o la contraseña son incorrectos')
#     else:
#         form=AuthenticationForm()
#     contexto={'formulario':form}
#     return render(request,'login.html',contexto)