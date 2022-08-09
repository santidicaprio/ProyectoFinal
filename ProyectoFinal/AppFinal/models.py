from django.db import models
from django.contrib.auth.models import User



class Productos(models.Model):
    marca= models.CharField(max_length=40)
    categoria= models.CharField(max_length=40)
    tipo= models.CharField(max_length=40)
    fecha_Vto = models.DateField()
    precio= models.IntegerField()
    image = models.ImageField(upload_to="productos", null=True)
    
    def __str__(self):
        return  f"{self.marca} {self.categoria} {self.tipo}"
    
    
class Contacto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    dni = models.CharField(max_length=40)
    mensaje = models.TextField()
    
    
class Empleado(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    nombre = models.CharField(max_length=40, null=True)
    apellido = models.CharField(max_length=40, null=True)
    imagen = models.ImageField(upload_to="empleado", null=True )
    fecha_de_alta = models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}"

    

