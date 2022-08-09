from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.views.generic import ListView, TemplateView, View, DetailView, DeleteView, UpdateView
from .models import Productos, Contacto, Empleado
from .forms import UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


@login_required
def dummy(request):
    render(request, "")


class PanelLogin(LoginView):
    template_name = 'Usuarios/login.html'
    next_page = reverse_lazy("panel-page")
          
class PanelLogout(LogoutView):
    template_name = 'Usuarios/logout.html'
    


class BaseView(View):

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Productos'] = Productos.objects.order_by('categoria')
        return context    

class About(BaseView, TemplateView):
    template_name = "principal/about.html"
    
class Contactame(CreateView):
    model = Contacto
    fields = ['usuario', 'dni', 'mensaje']
    template_name = "principal/contactame.html"
    success_url = reverse_lazy('main-page')
    

class MainPageView(BaseView, ListView):
    queryset = Productos.objects.all()
    context_object_name = "Productos"
    template_name = "principal/index.html"

class PanelView(LoginRequiredMixin, BaseView, ListView):
    queryset = Productos.objects.all()
    template_name = "Productos/productos.html"    
    context_object_name = "Productos"
    


class PorductosCreateView(LoginRequiredMixin, CreateView):
    model = Productos
    fields = ['marca','categoria', 'tipo', 'fecha_Vto', 'precio','image']
    template_name = "Productos/productosform.html"
    success_url = reverse_lazy("panel-page")
    
    
class detalleProductos(DetailView):

    model = Productos
    context_object_name = "Productos"
    template_name = "Productos/detalle_productos.html" 

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Productos'] = Productos.objects.order_by('categoria').first()
        return context
        

class eliminarProducto(LoginRequiredMixin, BaseView, DeleteView):
    model = Productos
    template_name = 'Productos/eliminar_producto.html'
    success_url = reverse_lazy("panel-page")

class editarProducto(LoginRequiredMixin, BaseView, UpdateView):  
    model = Productos
    fields = ['marca','categoria', 'tipo', 'fecha_Vto', 'precio', 'image']
    template_name = 'Productos/editar_productos.html'
    success_url = reverse_lazy('panel-page')

class PerfilEmpleado(LoginRequiredMixin, UserPassesTestMixin, DetailView):

    model = Empleado
    template_name = "Usuarios/empleado_detalle.html"
    context_object_name = "Empleado"
    
    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])



class EditarEmpleado(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = User
    template_name = "Usuarios/user_form.html"
    fields = ["email", "first_name", "last_name"]

    def get_success_url(self):
        return reverse_lazy("empleado-detalle", kwargs={"pk": self.request.user.id})
    
    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])
    

    
class crearCuentaUsuario(SuccessMessageMixin, CreateView):
  template_name = 'Usuarios/crear_cuenta_form.html'
  success_url = reverse_lazy('panel-page')
  form_class = UserCreationForm
  success_message = "¡¡ Se creo tu usuario satisfactoriamente !!"









    