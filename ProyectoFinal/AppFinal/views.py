from django.shortcuts import render
from urllib import request
from django.http import HttpResponse

from AppFinal.forms import MiFormulario


# Create your views here.
def saludo(request):
	return render(request, "AppFinal/proyecto.html")


def formulario(request):
    if request.method== 'POST':
        formu = MiFormulario(request.POST)
        print(formu)


    if formu.is_valid:
        informacion = MiFormulario.cleaned_data
        
        persona = MiFormulario(nombre=informacion['nombre'], apellido=informacion['apellido',])
        persona.save()

def index(req):
	return render(req, 'AppFinal/index.html')


    