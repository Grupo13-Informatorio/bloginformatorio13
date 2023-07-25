from datetime import datetime
from django.db import models
from apps.articulo.models import Articulo
from apps.usuario.models import Usuario

# Create your models here.

class Comentario(models.Model):
    
    contenido = models.CharField(
        max_length=200, 
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
    creado = models.DateTimeField(
        editable = False, 
        verbose_name = "Fecha de publicacion"
        )
    comentario_padre = models.ForeignKey(
        "self",
        on_delete = models.CASCADE, 
        verbose_name = 'Comentario',
        null = True,
        blank = True
        )
    usuario = models.ForeignKey(
        Usuario,
        on_delete = models.CASCADE,
        null=True,
        blank=True,
        verbose_name="creador", 
    )
    is_active = models.BooleanField(
        default=True,
    )    
    
    def __str__(self) -> str:
        return self.contenido
    
    def save(self, *args, **kwargs):
        self.creado = datetime.now()
        return super().save(*args, **kwargs)

