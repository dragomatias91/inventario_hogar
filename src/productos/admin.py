from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cantidad", "unidad_medida", "ubicacion", "disponible")
    search_fields = ("nombre",)
    list_filter=("disponible")