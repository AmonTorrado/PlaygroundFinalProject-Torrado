from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from . forms import CustomUserCreationForm

# Create your views here.
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