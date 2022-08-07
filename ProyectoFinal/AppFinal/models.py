from django.db import models



class Productos(models.Model):
    marca= models.CharField(max_length=40)
    categoria= models.CharField(max_length=40)
    tipo= models.CharField(max_length=40)
    fecha_Vto = models.DateField()
    precio= models.IntegerField()
    image = models.ImageField(upload_to="productos", null=True)
    
    def __str__(self):
        return  f"{self.marca} {self.categoria} {self.tipo}"

