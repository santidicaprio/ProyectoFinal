from unittest.util import _MAX_LENGTH
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MiFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email=forms.CharField(max_length=30)
    
## Modificacion de el formulario para registrarse

class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField()
    password1: forms.Field(label="Contraseña", widget= forms.PasswordInput)
    password2: forms.Field(label="Repetir Contraseña", widget= forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email', 'password1','password2']
        help_texts = {k:"" for k in fields}

    

