from django.db import models
from categorias.models import Categoria

class Producto(models.Model):

    class UnidadMedida(models.TextChoices):
        KG = 'KG', 'Kilogramo'
        GR = 'GR', 'Gramo'
        LT = 'LT', 'Litro'
        ML = 'ML', 'Mililitro'
        UNIDAD = 'UNIDAD', 'Unidad'

    class Ubicacion(models.TextChoices):
        ALACENA = 'ALACENA', 'Alacena'
        HELADERA = 'HELADERA', 'Heladera'
        FREEZER = 'FREEZER', 'Freezer'
        DESPENSA = 'DESPENSA', 'Despensa'

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    cantidad = models.IntegerField()
    unidad_medida = models.CharField(max_length=10, choices=UnidadMedida.choices)
    stock_minimo = models.IntegerField()
    fecha_vencimiento = models.DateField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    ubicacion = models.CharField(max_length=10, choices=Ubicacion.choices)
    disponible = models.BooleanField(default=True)