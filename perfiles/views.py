from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import PerfilUsuario
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.


class PerfilUsuarioCreateView(LoginRequiredMixin, CreateView):
    model = PerfilUsuario
    template_name = "crear_perfil.html"
    sucess_url = reverse_lazy("ver perfil")
    fields = ["usuario","imagen", "rol"]
    login_url = "/login"

@login_required(login_url="login")   
def crear_usuario(request):
       return render(request, "crear_perfil.html")       
    
class PerfilUsuarioUpdateView(LoginRequiredMixin, CreateView):
    model = PerfilUsuario
    template_name = "editar_perfil.html"
    success_url = reverse_lazy("ver perfil")
    fields = ["imagen", "rol"]
    login_url = "/login"
    
@login_required(login_url="login")
def perfil_usuario(request):
    try:
        request.user.perfil
        return render(request, "perfil.html")
    except:
        return redirect("crear perfil")