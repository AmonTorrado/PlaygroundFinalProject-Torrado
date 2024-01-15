from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50,blank=False, unique=True)
    nro_cuit = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return self.nombre + ", CUIT: " + str(self.nro_cuit)