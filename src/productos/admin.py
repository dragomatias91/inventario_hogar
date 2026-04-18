from django.contrib import admin
from .models import Producto , ListaCompras

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cantidad", "unidad_medida", "ubicacion", "disponible")
    search_fields = ("nombre",)
    list_filter=("disponible",)


@admin.register(ListaCompras)
class ListaComprasAdmin(admin.ModelAdmin):
    list_display = ("producto", "cantidad_necesaria", "comprado")
    list_filter = ("comprado",)
    search_fields = ("producto__nombre",)
