from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Esta clase hereada las propiedades de UserCreationForm 
# label es la etiqueta de los campos que tendra nuestro formulario
# Widget es el tipo de etiqueta que desea que sea 

#NOTA: La clase UserCreationForm esta configurada para usar por defecto la tabla "auth_user" por defecto que es donde se van a guadar los datos
class UserRegisterForm(UserCreationForm):
    username=forms.CharField(label='Nombre de usuario')
    email=forms.CharField(label='Correo',widget=forms.EmailInput)
    password1=forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirme contraseña',widget=forms.PasswordInput)
    # en la clase meta se indica que el modelo sera User y fields los campos que se desea aparezca en nuestro formulario  
    #por ultimo habra un for que recorrera fields y colocara una cadena en blanco, esto para borrar todos los textos de ayuda del formulario
    #en caso de que no se desee textos
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_texts={k:'' for k in fields}