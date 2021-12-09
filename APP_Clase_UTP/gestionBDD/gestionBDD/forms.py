from django import forms

class PeliculasForms(forms.Form):
    name=forms.CharField(label='Nombre')
    descripcion=forms.CharField(widget=forms.Textarea)
    categoria=forms.CharField()

class FormularioContacto(forms.Form):
    asunto=forms.CharField()
    email=forms.EmailField()
    mensaje=forms.CharField()