from django import forms
from .models import Producto, Categoria, Cliente

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'precio', 'descripcion')

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre', 'descripcion')

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'correo')

class BusquedaForm(forms.Form):
    busqueda = forms.CharField(max_length=100)