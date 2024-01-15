from django import forms
""" from .models import Producto """

class ProductoForm(forms.Form):
    nombre= forms.CharField()
    descripcion = forms.CharField()
    cantidad_en_stock = forms.IntegerField()
    otro_atributo = forms.CharField()
    precio = forms.IntegerField()
    imagen = forms.ImageField() 

class ProveedorFormulario(forms.Form):
    nombre= forms.CharField()
    nro_cel = forms.IntegerField()
    email = forms. EmailField()
    producto_asociado = forms.CharField()