from django.db import models

# Create your models here.

class Insumo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    unidad_de_medida = models.CharField(max_length=20)
    cantidad_en_stock = models.IntegerField()
    
    def __str__(self):
        return self.nombre + ' - ' + self.descripcion

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    cantidad_en_stock = models.IntegerField()
    
    def __str__(self):
        return self.nombre + ' - ' + self.descripcion
    
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
