from django.contrib import admin
from trabajo.models import Cliente, Venta, Insumo, Producto 

admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(Insumo)
admin.site.register(Producto)