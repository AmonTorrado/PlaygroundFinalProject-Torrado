from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Insumo, Producto
    
class Meta:
    model = User
    fields = ["username", "email", "password1", "password2"]
    help_texts = {k:"" for k in fields}
        
class ClienteFormulario(forms.Form):
    nombre= forms.CharField()
    nro_cuit = forms.IntegerField()
    email = forms. EmailField()
    
class InsumoForm(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField()
    unidad_de_medida = forms.CharField()
    cantidad_en_stock = forms.IntegerField()

class ProductoForm(forms.Form):
    class Meta:
        model = Producto
        fields = ['nombre', 'Descripción', 'Cantidad en stock']
