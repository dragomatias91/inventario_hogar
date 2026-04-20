from django import forms
from .models import Producto ,ListaCompras

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'cantidad', 'unidad_medida', 'stock_minimo', 'fecha_vencimiento', 'categoria', 'ubicacion', 'disponible']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'unidad_medida': forms.Select(attrs={'class': 'form-select'}),
            'stock_minimo': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_vencimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'ubicacion': forms.Select(attrs={'class': 'form-select'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class ListaComprasForm(forms.ModelForm):
    class Meta:
        model = ListaCompras
        fields = ['producto', 'cantidad_necesaria', 'comprado']
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-select'}),
            'cantidad_necesaria': forms.NumberInput(attrs={'class': 'form-control'}),
            'comprado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }