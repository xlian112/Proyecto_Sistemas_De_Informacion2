from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = [
            'nombre',
            'descripcion',
            'precio',
            'stock',
            'stock_minimo'
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Nombre del producto'
            }),

            'descripcion': forms.Textarea(attrs={
                'placeholder': 'Descripción del producto',
                'rows': 4
            }),

            'precio': forms.NumberInput(attrs={
                'min': '0',
                'step': '0.01'
            }),

            'stock': forms.NumberInput(attrs={
                'min': '0'
            }),

            'stock_minimo': forms.NumberInput(attrs={
                'min': '0'
            }),
        }