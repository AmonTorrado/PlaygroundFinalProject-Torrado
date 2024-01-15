from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    cantidad_en_stock = models.IntegerField()
    otro_atributo = models.CharField(max_length=50)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='imagenes_productos')
    
    def __str__(self):
        return self.nombre + ' - ' + self.descripcion #+ ' - ' + self.imagen

class Cliente(models.Model):
    nombre = models.CharField(max_length=50,blank=False, unique=True)
    nro_cuit = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return self.nombre + ", CUIT: " + str(self.nro_cuit)
    
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="ventas")
    nro_transaccion = models.IntegerField()
    producto = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    fecha_de_venta = models.DateField()
    
    def __str__(self):
        return "Venta nro: " + str(self.nro_transaccion)

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50,blank=False, unique=True)
    nro_cel = models.IntegerField()
    email = models.EmailField()
    producto_asociado = models.CharField(max_length=50)
