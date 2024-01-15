from django.urls import path
from .views import crear_producto,busqueda_en_bd, lista_en_stock, crear_proveedor,comprar_producto, editar_proveedores,lista_proveedores,editar_producto, eliminar_proveedores,leer_proveedores, ProveedorCreateView, ProveedorDeleteView, ProveedorDetailView, ProveedorUpdateView,ProductoUpdateView, ProductoCreateView, ProductoDeleteView, ProductoDetailView

urlpatterns = [
  path('crear_producto', crear_producto, name='crear producto'),
  path('busquedaBD', busqueda_en_bd, name='busquedaBD'),
  path('listaStock', lista_en_stock.as_view(), name='listaStock'),
  path('crear_proveedor', crear_proveedor, name='crear proveedor'),
  path('editar_proveedores', editar_proveedores, name='editar proveedores'),
  path('editar_producto', editar_producto, name='editar producto'),
  path('comprarProducto', comprar_producto, name='comprarProducto'),
  path('eliminar_proveedores', eliminar_proveedores, name='eliminar proveedores'),
  path('leer_proveedores', leer_proveedores, name='leer proveedores'),
  path('<pk>/eliminar/', ProveedorDeleteView.as_view(), name='proveedor eliminar'),
  path('<pk>/editar/', ProveedorUpdateView.as_view(), name='proveedor editar'),
  path('<pk>/detalle/', ProveedorDetailView.as_view(), name='proveedor detalle'),
  path('lista_proveedores', lista_proveedores.as_view(), name='proveedores lista'),
  path('<pk>/eliminarProducto/', ProductoDeleteView.as_view(), name='producto eliminar'),
  path('<pk>/editarProducto/', ProductoUpdateView.as_view(), name='producto editar'),
  path('<pk>/detalleProducto/', ProductoDetailView.as_view(), name='producto detalle'),
]