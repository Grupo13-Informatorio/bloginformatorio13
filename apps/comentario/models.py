from datetime import datetime
from django.db import models
from apps.articulo.models import Articulo

# Create your models here.

class Comentario(models.Model):
    
    contenido = models.CharField(
        max_length=100, 
        verbose_name='Texto', 
        help_text='Ingrese aqui su comentario',
        default = ''
        )
    articulo = models.ForeignKey(
        Articulo, 
        on_delete = models.CASCADE, 
        verbose_name = 'Articulo',
        null = True,
        blank = True
        )
    creado = models.DateField(
        default= datetime.now(),
        editable = False, 
        verbose_name = "Fecha de publicacion"
        )

    
    def __str__(self) -> str:
        return self.contenido

