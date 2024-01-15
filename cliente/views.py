from django.shortcuts import render, redirect
from .forms import ClienteFormulario
from .models import Cliente
from django.contrib.auth.decorators import login_required

# Create your views here.
def leer_clientes(request):
    lista_clientes = Cliente.objects.all()
    return render(request, "lista_proveedores.html", {"clientes": lista_clientes})

def eliminar_cliente(request, nombre_cliente):
    cliente = Cliente.objects.get(nombre=nombre_cliente)
    cliente.delete()
    return redirect('leer clientes')

def editar_cliente(request, nombre_cliente):
    cliente = Cliente.objects.get(nombre=nombre_cliente)
    
    if request.method == "POST":
        mi_formulario = ClienteFormulario(request.POST) # Aqui me llega la informacion del html

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            cliente.nombre = informacion['nombre']
            cliente.nro_cuit = informacion['nro_cuit']
            cliente.email = informacion['email']
            cliente.save()
            return render(request, "index.html")
    else:
        mi_formulario = ClienteFormulario()
        return render(request, "editar_cliente.html", {"mi_formulario": mi_formulario})

def crear_cliente(request):
    if request.method == "POST":
        mi_formulario = ClienteFormulario(request.POST) # Aqui me llega la informacion del html
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            cliente = Cliente(
                nombre=informacion["nombre"],
                nro_cuit=informacion["nro_cuit"],
                email=informacion["email"]
                )
            cliente.save()
            return render(request, "index.html")
        else:
            return render(request, 'crear_cliente.html', {"errors": mi_formulario.errors})
    else:
        mi_formulario = ClienteFormulario()
        return render(request, "crear_cliente.html", {"mi_formulario": mi_formulario})