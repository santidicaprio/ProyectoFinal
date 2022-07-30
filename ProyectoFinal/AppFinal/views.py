from django.shortcuts import render
from urllib import request
from django.http import HttpResponse
from AppFinal.forms import MiFormulario
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
    
 ## Desde aca agregue las ClassBase Views   

class PanelLogin(LoginView):
    template_name = 'Usuarios/login.html'
    next_page = reverse_lazy("panel-login")## cambiar panel-login por pagina portal de productos

class PanelLogout(LogoutView):
    template_name = 'Usuarios/incio.html' ## cambiar panel-login por pagina portada
    
## creacion del usuario
class signUpView(SuccessMessageMixin, CreateView):
    template_name = 'Usuarios/registro.html'
    success_url= reverse_lazy("registrate")
    form_classc= UserCreationForm ##cuando funcione recordar poner el Formulario modificado
    success_message ="Usuario Creado con Exito!"

# Hasta Aca



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


    