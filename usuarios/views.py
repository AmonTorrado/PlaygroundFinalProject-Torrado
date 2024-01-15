from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import PerfilUsuario
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from . forms import CustomUserCreationForm

# Create your views here.
def index(request):
    return render(request,"inicio.html")

def login_request(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            
            login(request, user)
            if request.user.is_superuser:
                return render(request, "base.html", {"mensaje": f'Bienvenido admin {user.username}'})
            else:
                return render(request, "index.html", {"mensaje": f'Bienvenido {user.username}'})
        else:
            return render(request, "login.html", {"formulario": formulario})
    
    else:
        formulario = AuthenticationForm()
        return render(request, "login.html", {"formulario": formulario})
    
class Logout(LogoutView):
    template_name = "logout.html"


@login_required(login_url="login")   
def crear_usuario(request):
       return render(request, "crear_perfil.html")   
   
class PerfilUsuarioCreateView(LoginRequiredMixin, CreateView):
    model = PerfilUsuario
    template_name = "crear_perfil.html"
    sucess_url = reverse_lazy('ver perfil')
    fields = ["usuario","alias","imagen", "rol"]
    login_url = "/login"
    

@login_required(login_url="login")   
def crear_usuario(request):
       return render(request, "crear_perfil.html")       
    
class PerfilUsuarioUpdateView(LoginRequiredMixin, CreateView):
    model = PerfilUsuario
    template_name = "editar_perfil.html"
    success_url = reverse_lazy("ver perfil")
    fields = ["alias","imagen", "rol"]
    login_url = "login"
    
@login_required(login_url="login")
def perfil_usuario(request):
    try:
        request.user.perfil
        return render(request, "perfil.html")
    except:
        return redirect('ver perfil')

def registro(request):

    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            formulario.save()
            return render(request,"inicio.html" ,  {"mensaje":"Usuario " + username + " registrado"})
        else:
            return render(request, 'registro.html', {"formulario": formulario})

    else:
        formulario = CustomUserCreationForm()
        return render(request,"registro.html" ,  {"formulario": formulario})