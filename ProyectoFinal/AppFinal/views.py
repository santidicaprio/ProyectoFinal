from django.shortcuts import render
from urllib import request
from django.http import HttpResponse
from AppFinal.forms import MiFormulario
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.views.generic import ListView, TemplateView, View, DetailView, DeleteView
from .models import Productos
from .forms import UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin



# Loguearse

class PanelLogin(LoginView):
    template_name = 'Usuarios/login.html'
    next_page = reverse_lazy("panel-login")
        
class PanelLogout(LogoutView):
    template_name = 'principal/index.html'   
    
## creacion del usuario
def registro(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data['username']
            form.save()
            return render(request, "Usuarios/login.html", {"mensajes": "Usuario Creado"} )
    else:
        form = UserRegisterForm()
    return render(request, "Usuarios/registro.html", {"form": form})


# 


#pagina Principal

class BaseView(View):

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Productos'] = Productos.objects.order_by('categoria')
        return context    

class About(BaseView, TemplateView):

    template_name = "principal/about.html"

class MainPageView(BaseView, ListView):
    queryset = Productos.objects.all()
    context_object_name = "Productos"
    template_name = "principal/index.html"
    
    
##

## baseviews productos (Falta borrar y editar producto)

class PorductosCreateView(LoginRequiredMixin, CreateView):
    model = Productos
    fields = ['marca','categoria' , 'tipo', 'fecha_Vto', 'precio','image']
    template_name = "productos/productosform.html"
    success_url = reverse_lazy("panel-page")



class PanelView(LoginRequiredMixin, BaseView, ListView):
    
    queryset = Productos.objects.all()
    template_name = "productos/productos.html"    
    context_object_name = "Productos"
    
    
class ProductoDetailView(DetailView):

    model = Productos
    context_object_name = "Productos"
    template_name = "productos/detalle_productos.html" 

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Productos'] = Productos.objects.order_by('categoria').first()
        return context
    
    
## Hasta aca modificacion 

class eliminarProducto(DeleteView):
    model = Productos
    template_name = 'productos/eliminar_producto.html'
    success_url = reverse_lazy("panel-page")










    