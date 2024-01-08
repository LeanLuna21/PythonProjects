from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    medida = models.CharField(max_length=10)
    color_sable = models.CharField(max_length=50)
    color_luz = models.CharField(max_length=50)
    stock = models.IntegerField()
    descripcion = models.TextField()
    precio = models.FloatField(default=0)

    def __str__(self):
        return f"Producto: {self.nombre}."
