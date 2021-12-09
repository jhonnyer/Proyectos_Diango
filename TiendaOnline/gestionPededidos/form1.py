from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(label='Nombre de usuario')
    direccion = forms.CharField()
    email=forms.EmailField()
    telefono= forms.CharField()


    # def send_email(self):
    #     # send email using the self.cleaned_data dictionary
    #     pass


