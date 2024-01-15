from django.shortcuts import render, redirect
from .forms import ProveedorFormulario, ProductoForm
from .models import Producto
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Proveedor

# Create your views here.
""" ################# SECCIÓN DE PRODUCTO ##########################
################################################################
 """
login_required(login_url="login")    
def busqueda_en_bd(request):
    if request.GET.get("nombre", False):
        busqueda = request.GET["nombre"]
        lista_productos = Producto.objects.filter(nombre__icontains=busqueda)
        return render(request, 'busqueda.html', {'lista': lista_productos})
    else:
        lista_productos=Producto()
        return render(request, 'busqueda.html')

def comprar_producto(request):
    if request.method == "POST":
        busqueda = request.POST["nombre"]
        producto = Producto.objects.get(nombre=busqueda)
        cantidad_compra = int(request.POST["cantidad"])
        # Modificar el stock del producto y guardarlo en la base de datos:
        producto.cantidad_en_stock = producto.cantidad_en_stock - cantidad_compra
        producto.save()
        return render(request, 'comprar_producto.html', {'producto': producto.nombre, 'cantidad_stock': producto.cantidad_en_stock})
    else:
        return render(request, 'comprar_producto.html')

login_required(login_url="login")
def crear_producto(request):
    if request.method == "POST":
            formu=ProductoForm(request.POST)
            if  formu.is_valid():
                info = formu.cleaned_data  
                producto = Producto(
                nombre = info["nombre"],
                descripcion = info["descripcion"],
                cantidad_en_stock = info["cantidad_en_stock"],
                otro_atributo=info["otro_atributo"],
                precio=info["precio"],
                imagen = info["imagen"]
                )
                print("hasta aca llego")
                producto.save()
                return render(request, "inicio.html")
            else:
                print("no entro")
                return render(request, "inicio.html")
    else:
        formu = ProductoForm()
        return render(request, 'producto_formulario.html',{"formu": formu})
    
def editar_producto(request, nombre_producto):
    producto = Producto.objects.get(nombre=nombre_producto)
    
    if request.method == "POST":
        mi_form = ProductoForm(request.POST) # Aqui me llega la informacion del html
        if mi_form.is_valid():
            informacion = mi_form
            producto.nombre = informacion['nombre']
            producto.descripcion = informacion['descripcion']
            producto.cantidad_en_stock = informacion['cantidad_en_stock']
            producto.otro_atributo=informacion['otro_atributo']
            producto.save()
            return render(request, "index.html")
    else:
        mi_form = ProductoForm()
        return render(request, "producto_editar.html", {"mi_form": mi_form})

class lista_en_stock(ListView):
    model = Producto
    context_object_name = "stock"
    template_name = "lista_stock.html"

class ProductoCreateView(CreateView):
    model = Producto
    template_name = "producto_formulario.html"
    success_url = reverse_lazy('listaStock')
    fields = ['nombre', 'descripcion', 'cantidad_en_stock','otro_atributo','precio','imagen']

class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = "producto_editar.html"
    success_url = reverse_lazy("listaStock")
    fields = ['nombre', 'descripcion', 'cantidad_en_stock','otro_atributo','precio','imagen']

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "producto_eliminar.html"
    success_url = reverse_lazy("listaStock")

class ProductoDetailView(DetailView):
    model = Producto
    template_name = "producto_detalle.html"
    success_url = reverse_lazy("listaStock")
    
""" ###########################################################
    ###########################################################
    
  ################ SECCIÓN DE PROVEEDORES ##################### 
  ############################################################# """
  
class ProveedorCreateView(CreateView):
    model = Proveedor
    template_name = "crear_proveedor.html"
    success_url = reverse_lazy('proveedores lista')
    fields = ['nombre', 'cel', 'email']

class ProveedorUpdateView(UpdateView):
    model = Proveedor
    template_name = "proveedor_editar.html"
    success_url = reverse_lazy("proveedores lista")
    fields = ['nombre', 'nro_cel', 'email']

class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = "proveedor_eliminar.html"
    success_url = reverse_lazy("proveedores lista")

class ProveedorDetailView(DetailView):
    model = Proveedor
    template_name = "proveedor_detalle.html"
    success_url = reverse_lazy("proveedores lista")
    model = Proveedor
    template_name = "proveedor_detalle.html"
    success_url = reverse_lazy("proveedores lista")
    
def leer_proveedores(request):
    lista_proveedores = Proveedor.objects.all()
    return render(request, "lista_proveedores.html", {"proveedores": lista_proveedores})

def eliminar_proveedores(request, nombre_proveedor):
    proveedor = Proveedor.objects.get(nombre=nombre_proveedor)
    proveedor.delete()
    return redirect('leer proveedores')

def editar_proveedores(request, nombre_proveedor):
    proveedor = Proveedor.objects.get(nombre=nombre_proveedor)
    
    if request.method == "POST":
        mi_formulario = ProveedorFormulario(request.POST) # Aqui me llega la informacion del html
        if mi_formulario.is_valid():
            informacion = mi_formulario
            proveedor.nombre = informacion['nombre']
            proveedor.nro_cel = informacion['nro_cel']
            proveedor.email = informacion['email']
            proveedor.producto_asociado=informacion['producto_asociado']
            proveedor.save()
            return render(request, "index.html")
    else:
        mi_formulario = ProveedorFormulario()
        return render(request, "proveedor_editar.html", {"mi_formulario": mi_formulario})

def crear_proveedor(request):
    if request.method == "POST":
        mi_formulario = ProveedorFormulario(request.POST) # Aqui me llega la informacion del html
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            proveedor = Proveedor(
                nombre=informacion["nombre"],
                nro_cel=informacion["nro_cel"],
                email=informacion["email"],
                producto_asociado=informacion["producto_asociado"]
                )
            proveedor.save()
            return render(request, "creacion_exitosa.html")
        else:
            return render(request, 'crear_proveedor.html', {"errors": mi_formulario.errors})
    else:
        mi_formulario = ProveedorFormulario()
        return render(request, "crear_proveedor.html", {"mi_formulario": mi_formulario})

class lista_proveedores(ListView):
    model = Proveedor
    context_object_name = "proveedores"
    template_name = "lista_proveedores.html"

""" ################################################
################################################
   """