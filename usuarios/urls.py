from django.urls import path
from django.conf.urls.static import static
from .views import index, login_request, Logout, perfil_usuario, PerfilUsuarioUpdateView, PerfilUsuarioCreateView,registro
from django.conf import settings


urlpatterns = [
    path('login/', login_request, name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('crear_perfil/', PerfilUsuarioCreateView.as_view(),name = 'crear perfil'),
    path('<pk>/editar_perfil/', PerfilUsuarioUpdateView.as_view(), name='editar perfil'),
    path('perfil_usuario/', perfil_usuario, name='ver perfil'),
    path('registro', registro, name='registro')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)