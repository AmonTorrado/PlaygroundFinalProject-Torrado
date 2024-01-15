from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class PerfilUsuario(models.Model):
    CHOICE = (
        ('cliente', 'cliente'),
        ('vendedor', 'vendedor')
    )
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    alias= models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='imagenes_usuarios')
    rol = models.CharField(max_length=10, choices=CHOICE, null=True, blank=True)
    def get_absolute_url(self): # new
        return reverse('ver perfil')
    
    def __str__(self):
        return "Usuario: " + self.usuario.username + ", Rol del usuario: " + str(self.rol)