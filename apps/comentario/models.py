from django.db import models
from django.contrib.auth.models import User
from apps.articulo.models import Articulo



# Create your models here.

class Comentario(models.Model):
    comentario = models.CharField(
        max_length=100, 
        verbose_name='Comentario', 
        help_text='Ingrese aqui su comentario'
        )
    articulo = models.ForeignKey(
        Articulo, 
        on_delete = models.SET_NULL, 
        null=True, 
        verbose_name = 'Articulo'
        )
    fecha = models.DateField(
        auto_now = True, 
        verbose_name = "Fecha de publicacion"
        )
    # imagen = models.ImageField(
    #     null = True
    # )
    
    def __str__(self) -> str:
        return self.comentario
    