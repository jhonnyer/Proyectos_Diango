from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(label='Nombre de usuario')
    direccion = forms.CharField()
    email=forms.EmailField()
    telefono= forms.CharField()
