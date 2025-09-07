from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)
    descripcion = models.CharField(max_length=2500, default= '', blank=True, null=True)
    imagen = models.ImageField(upload_to='uploads/producto/')

    def __str__(self):
        return self.nombre
    


