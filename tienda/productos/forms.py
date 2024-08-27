from django import forms
from .models import Producto, Cliente
from django.contrib.auth.forms import UserCreationForm

# class Productoforms(forms.Form):
#     nombre = forms.CharField(max_length=100)
#     descripcion = forms.CharField(widget=forms.Textarea)
#     precio = forms.DecimalField(max_digits=10, decimal_places=2)
#     stock = forms.IntegerField()

class ProductoModelForm(forms.ModelForm):
    class Meta:
        model= Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock']

    #validacion personalizada para el campo de precio
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio <= 0: #con esta validacion nos aseguramos que aparezca un error si el precio es menor a cero.
            raise forms.ValidationError('El precio debe ser mayor que cero. ')
        return precio

class ClienteModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono']

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Cliente
        fields = ['username', 'email', 'password1', 'password2']