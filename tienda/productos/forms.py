from django import forms
from .models import Producto

# class Productoforms(forms.Form):
#     nombre = forms.CharField(max_length=100)
#     descripcion = forms.CharField(widget=forms.Textarea)
#     precio = forms.DecimalField(max_digits=10, decimal_places=2)
#     stock = forms.IntegerField()

class ProductoModelForm(forms.ModelForm):
    class Meta:
        model= Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock']