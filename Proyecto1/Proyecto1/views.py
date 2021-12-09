from Proyecto1.settings import TEMPLATES
from django.http import HttpResponse
import datetime #importo libreria de fechas
from django.template import Template, Context, loader
#Simplificar codigo con get_template para las plantillas
from django.template.loader import get_template
#Simplificar renderizar plantilla con modulo shortcuts, importar metodo render
from django.shortcuts import render

# Crear clase persona 
class Persona(object):
    def __init__(self,name,apellido):
        self.name=name
        self.apellido=apellido


#Recibe un request como primer argumento de la lista
#Cada funcion creada en el archivo views.py se le denomina vista
def saludo(request):
    # return HttpResponse("<HTML><body><h1>Hola mundo, primer pagina con django</h1></body></HTML>")
    # documento="<HTML><body><h1>Hola mundo, primer pagina con django</h1></body></HTML>"
    #  documento="""<HTML>
    #                     <body>
    #                         <h1>Hola mundo, primer pagina con django
    #                         </h1>
    #                     </body>
    #                 </HTML>"""
     # Cargar archivo html desde un documento externo 
    doc_externo=open("/home/jhonnyer/Documentos/Proyectos_Django/Proyecto1/Proyecto1/Plantillas/index.html")
    # Creo el objeto de tipo template, importar clase Template
    # La variable plt me va a tener almacenado la vista
    plt=Template(doc_externo.read())
    #Cerramos el flujo de la comunicacion para no consumir recursos de mas
    doc_externo.close()
    #Creamos el contexto, se debe importar clase context
    ctx=Context()
    #Renderizamos el documento
    documento=plt.render(ctx)
    return HttpResponse(documento)

def despedida(request):    #Cargamos plantilla, en el archivo settings indicamos la carpeta donde estan las plantillas
    # doc_externo=loader.get_template('fecha.html')
    #utilizar lenguaje mas simplificado utiliando solo get_template()
    doc_externo=get_template('fecha.html')
    return HttpResponse("Hasta luego")

def dameFecha(request):
    # Siguiente funcion devuelve fecha y hora actual 
    fecha_actual=datetime.datetime.now()
    # %s es un marcador de posision, hace referencia a una variable 
    # Cargar archivo html 
    # documento="""<HTML>
    #                     <body>
    #                         <h1>Fecha y hora actual %s
    #                         </h1>
    #                     </body>
    #                 </HTML>"""% fecha_actual

    # Crear objeto de la clase persona 
    p1=Persona("Juan","Diaz")

    # Utilizar variable en las plantillas 
    nombre="Jhonnyer"

    # Cargar archivo html desde un documento externo 
    doc_externo=open("/home/jhonnyer/Documentos/Proyectos_Django/Proyecto1/Proyecto1/Plantillas/fecha.html")
    # Creo el objeto de tipo template, importar clase Template
    # La variable plt me va a tener almacenado la vista
    plt=Template(doc_externo.read())
    #Cerramos el flujo de la comunicacion para no consumir recursos de mas
    doc_externo.close()
    #Creamos el contexto, se debe importar clase context
    #Pasar un valor de una variable, en este caso valor almacenado en la variable nombre
    # ctx=Context({'fecha_actual':fecha_actual,'nombre':nombre,'apellido':'Galindez'})
    # Voy a hacer referencia al nombre del objeto p1, utilizo el punto(.) para acceder a sus propiedades
    #pasar una lista ejemplo temas=>  "temas":["Plantillas","Modelos","Base de datos"]
    #pasar lista en una variable
    lenguaje=["PHP","Javascript","HTML"]
    lista_vacia=[]
    ctx=Context({'fecha_actual':fecha_actual,'nombre':p1.name,'apellido':p1.apellido,'temas':["Plantillas","Modelos","Base de datos"],'lenguaje':lenguaje, 'lista_vacia':lista_vacia})
    #Renderizamos el documento
    documento=plt.render(ctx)
    return HttpResponse(documento)  

def calculaEdad(request,agno):
    edadActual=18
    periodo=agno-2021
    edadFuturo=edadActual+periodo
    documento="<html><body><h2>En el año %s tendrás %s años <h2><body><html>" % (agno,edadFuturo)
    return HttpResponse(documento)

#Recibe dos parametros
def calculaEdades(request,edad,agno):
    #edadActual=18; voy a recibirlo por parametro edad
    periodo=agno-2021
    edadFuturo=edad+periodo
    x=sumar()
    documento="<html><body><h2>En el año %s tendrás %s años. Suma %s <h2><body><html>" % (agno,edadFuturo,x)
    return HttpResponse(documento)

def sumar():
    n=3
    m=5
    x=n+m
    return x


def loader_plantilla(request):
    # Siguiente funcion devuelve fecha y hora actual 
    fecha_actual=datetime.datetime.now()
    # Crear objeto de la clase persona 
    p1=Persona("Jhonnyer","Galindez")
    
    #Cargamos plantilla, en el archivo settings indicamos la carpeta donde estan las plantillas
    # doc_externo=loader.get_template('fecha.html')
    #utilizar lenguaje mas simplificado utiliando solo get_template()
    doc_externo=get_template('fecha.html')
    #Creamos el contexto, se debe importar clase context
    #pasar lista en una variable
    lenguaje=["PHP","Javascript","HTML"]
    lista_vacia=[]
    #Renderizamos el documento
    # documento=doc_externo.render({'fecha_actual':fecha_actual,'nombre':p1.name,'apellido':p1.apellido,'temas':["Plantillas","Modelos","Base de datos"],'lenguaje':lenguaje, 'lista_vacia':lista_vacia})
    diccionario={'fecha_actual':fecha_actual,'nombre':p1.name,'apellido':p1.apellido,'temas':["Plantillas","Modelos","Base de datos"],'lenguaje':lenguaje, 'lista_vacia':lista_vacia}
    documento=doc_externo.render(diccionario)
    return HttpResponse(documento)  

def loader_short_plantilla(request):
    # Siguiente funcion devuelve fecha y hora actual 
    fecha_actual=datetime.datetime.now()
    # Crear objeto de la clase persona 
    p1=Persona("Jhonnyer","Galindez")
    
    #Creamos el contexto, se debe importar clase context
    #pasar lista en una variable
    lenguaje=["PHP","Javascript","HTML"]
    lista_vacia=[]
    #Renderizamos el documento
    # documento=doc_externo.render({'fecha_actual':fecha_actual,'nombre':p1.name,'apellido':p1.apellido,'temas':["Plantillas","Modelos","Base de datos"],'lenguaje':lenguaje, 'lista_vacia':lista_vacia})
    diccionario={'fecha_actual':fecha_actual,'nombre':p1.name,'apellido':p1.apellido,'temas':["Plantillas","Modelos","Base de datos"],'lenguaje':lenguaje, 'lista_vacia':lista_vacia}
    #Cargamos el request, la plantilla y el diccionario en una sola linea renderizada
    return render(request,'fecha.html',diccionario)

def curso_django(request):
    fecha_actual=datetime.datetime.now()
    return render(request,'Curso_Django.html',{"dameFecha":fecha_actual})

def curso_css(request):
    fecha_actual=datetime.datetime.now()
    return render(request,'cursoCss.html',{"dameFecha":fecha_actual})

def sumar1(a,b):
    x=a+b
    return x


# def tareas(request):
#     a=10
#     b=20
#     c=sumar1(a,b)
#     Tareas=['Aprender sobre el internet','Aprender Python','Aprender HTML','Aprender CSS','Practicar python','Aprender Django','Crear mi página web']
#     doc_externo=get_template('tareas.html')
#     documento=doc_externo.render({'listado':Tareas,'a':a,'b':b,'c':c})
#     return HttpResponse(documento)


def tareas(request):
    a=10
    b=20
    c=sumar1(a,b)
    Tareas=['Aprender sobre el internet','Aprender Python','Aprender HTML','Aprender CSS','Practicar python','Aprender Django','Crear mi página web']
    return render(request,'tareas.html',{'listado':Tareas,'a':a,'b':b,'c':c})


def tareasprueba(request,a,b):
    c=sumar1(a,b)
    Tareas=['Aprender sobre el internet','Aprender Python','Aprender HTML','Aprender CSS','Practicar python','Aprender Django','Crear mi página web']
    return render(request,'tareas.html',{'listado':Tareas,'a':a,'b':b,'c':c})


def games(request):
    anio=datetime.datetime.now().year
    dia=datetime.datetime.now().day
    mes=datetime.datetime.now().month
    hora=datetime.datetime.now().strftime('%X')
    fecha='%s/%s/%s a las %s' %(dia, mes, anio, hora)
    return render(request,'games.html',{'fecha':fecha})


def musica(request):
    anio=datetime.datetime.now().year
    dia=datetime.datetime.now().day
    mes=datetime.datetime.now().month
    hora=datetime.datetime.now().strftime('%X')
    fecha='%s/%s/%s a las %s' %(dia, mes, anio, hora)
    return render(request,'musica.html',{'fecha':fecha})


def tecnologias(request):
    anio=datetime.datetime.now().year
    dia=datetime.datetime.now().day
    mes=datetime.datetime.now().month
    hora=datetime.datetime.now().strftime('%X')
    fecha='%s/%s/%s a las %s' %(dia, mes, anio, hora)
    return render(request,'tecnologias.html',{'fecha':fecha})
