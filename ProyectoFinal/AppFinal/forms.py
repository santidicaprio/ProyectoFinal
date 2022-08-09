from unittest.util import _MAX_LENGTH
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

    
## Modificacion de el formulario para registrarse

class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField()
    password1: forms.Field(label="Contraseña", widget= forms.PasswordInput)
    password2: forms.Field(label="Repetir Contraseña", widget= forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()
    
    class Meta:
        model = User
        fields = ['email', 'password1','password2','last_name','first_name']
        help_texts = {k:"" for k in fields}
        



