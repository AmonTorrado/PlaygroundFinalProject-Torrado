from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate

# Create your views here.
def login_request(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            
            login(request, user)
            return render(request, "index.html", {"mensaje": f'Bienvenido {user.username}'})
        else:
            return render(request, "login.html", {"formulario": formulario})
    
    else:
        formulario = AuthenticationForm()
        return render(request, "login.html", {"formulario": formulario})
    
class Logout(LogoutView):
    template_name = "logout.html"