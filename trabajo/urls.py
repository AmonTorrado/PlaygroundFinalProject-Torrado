from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import crear_producto,VentaCreateView, VentaDeleteView, VentaUpdateView, VentaDetailView

urlpatterns = [
    path("", views.index, name='Index'),
    path('leer_clientes', views.leer_clientes, name='leer clientes'),
    path('eliminar_cliente/<nombre_cliente>', views.eliminar_cliente, name='eliminar cliente'),
    path('editar_cliente/<nombre_cliente>', views.editar_cliente, name='editar cliente'),
    path('listaVentas', views.lista_ventas.as_view(), name='listaVentas'),
    path('crear_cliente', views.crear_cliente, name='crear cliente'),
    path('comprarProducto', views.comprar_producto, name='comprarProducto'),
    path('crear_insumo', views.crear_insumo, name='crear insumo'),
    path('crear_producto', crear_producto, name='crear producto'),
    path('busquedaBD', views.busqueda_en_bd, name='busquedaBD'),
    path('ventas_crear/', VentaCreateView.as_view(), name='ventas crear'),
    path('<pk>/eliminar/', VentaDeleteView.as_view(), name='ventas eliminar'),
    path('<pk>/editar/', VentaUpdateView.as_view(), name='ventas editar'),
    path('<pk>/detalle/', VentaDetailView.as_view(), name='ventas detalle'),
    path('inicio', views.inicio, name='inicio'),
    path('about', views.about, name='about'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)