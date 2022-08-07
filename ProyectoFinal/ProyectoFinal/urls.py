"""ProyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from AppFinal.views import PanelLogin, MainPageView, About, PanelView, registro, PorductosCreateView, ProductoDetailView, eliminarProducto
 


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', MainPageView.as_view(), name='main-page'),
    path('about/', About.as_view(), name="about"),
    path('panel/', PanelView.as_view(), name='panel-page'),
    path("login/", PanelLogin.as_view(), name="panel-login"),
    path("registrate/", registro , name= "registrate"),
    path('productos/crear', PorductosCreateView.as_view(), name ="crear-producto" ),
    path('detalle/productos/<pk>/', ProductoDetailView.as_view(), name="detalle-producto"),
    path('eliminarProducto/<pk>/delete', eliminarProducto.as_view(), name="eliminar-producto"),

    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
