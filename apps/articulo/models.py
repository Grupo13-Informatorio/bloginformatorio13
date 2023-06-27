from collections import UserList
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Articulo(models.Model):
    
    fecha = models.DateField(auto_now = True, verbose_name = "Fecha de publicacion")
    titulo = models.CharField(max_length=100, verbose_name="Titulo", help_text="Ingrese el titulo del articulo")
    resumen = models.TextField(verbose_name= 'Resumen', help_text='Ingrese aqui su resumen')
    contenido = models.TextField(verbose_name= "Contenido", help_text="Ingrese aqui el contenido del articulo")
    usuario = models.ForeignKey(User, on_delete = models.SET_NULL, null=True, verbose_name = 'Autor')
