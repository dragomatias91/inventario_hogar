from django.db import models

class Categoria(models.Model):
    nombre= models.CharField(max_length=20)
    descripcion= models.TextField()
