
from django.urls import path
from .views import crear_cliente, leer_clientes, eliminar_cliente, editar_cliente
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('leer_clientes', leer_clientes, name='leer clientes'),
    path('eliminar_cliente/<nombre_cliente>', eliminar_cliente, name='eliminar cliente'),
    path('editar_cliente/<nombre_cliente>', editar_cliente, name='editar cliente'),
    path('crear_cliente', crear_cliente, name='crear cliente')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)     