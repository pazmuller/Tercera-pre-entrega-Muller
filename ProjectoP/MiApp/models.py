from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    class Meta:
        db_table = "MiApp_categoria"

class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    correo = models.EmailField()

