from .models import Producto, Categoria
from django import forms

class crearProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock', 'talla', 'categoria', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingresa el nombre del producto', 'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'placeholder': '0', 'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'placeholder': 'Cantidad en stock', 'class': 'form-control'}),
            'talla': forms.TextInput(attrs={'placeholder': 'Talla del producto (opcional)', 'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class crearCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre de la categoría', 'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'placeholder': 'Descripción de la categoría', 'class': 'form-control', 'rows': 3}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
