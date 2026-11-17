from django import forms
from .models import Productos


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['sku', 'nombre', 'descripcion', 'estado' ,'precio', 'stock_disponible','fecha_ingreso', 'categoria']
        widgets = {
            'sku': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'stock_disponible': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
        }
        