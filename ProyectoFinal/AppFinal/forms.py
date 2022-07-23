from unittest.util import _MAX_LENGTH
from django import forms

class MiFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email=forms.CharField(max_length=30)
    

