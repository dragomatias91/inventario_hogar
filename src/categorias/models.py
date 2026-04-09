from django.db import models

class Categoria(models.Model):
    nombre= models.CharField(max_length=20)
    descripcion= models.TextField(null=True , blank=True )

    def __str__(self):
        return f"{self.nombre.upper()}"
