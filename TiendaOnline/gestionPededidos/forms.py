from django import forms
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView
from .form1 import ContactForm
from gestionPededidos.models import Cliente
from django.shortcuts import redirect, render

class FormularioContacto(forms.Form):
    asunto=forms.CharField()
    email=forms.EmailField()
    mensaje=forms.CharField()


#Verifica que el formulario sea valido y retorna hacia la url de exito
class formView_prueba(FormView):
    form_class=ContactForm
    template_name='contact.html'
    success_url='/gracias/'

    def form_valid(self,form):
        return super().form_valid(form)

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
            Cliente.objects.create(nombre=nombre,direccion=direccion,email=email,telefono=telefono)
            return render(request, 'gracias.html',{'username':nombre})
        return render(request, 'gracias.html')

    # def get_context_data(self, **kwargs):
    #     context=super().get_context_data(**kwargs)
    #     context['username']='Form | Contacto'
    #     context['entity']='Contacto'
    #     context['list_url']='/gracias/'
    #     context['action']='add'
    #     return context
    
class AuthorCreateView(CreateView):
    model = Cliente
    fields = ['nombre','direccion','email','telefono']