from django.urls import path, include
from . views import perfil_usuario, PerfilUsuarioCreateView, PerfilUsuarioUpdateView, crear_usuario
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('crear_perfil', PerfilUsuarioCreateView.as_view(),name = 'crear perfil'),
    path('<pk>/editar_perfil', PerfilUsuarioUpdateView.as_view(), name='editar perfil'),
    path('perfil_usuario', perfil_usuario, name='ver perfil')
]