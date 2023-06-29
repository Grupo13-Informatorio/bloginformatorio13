import datetime
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
    modificado = models.DateField(
        editable = True,
        verbose_name = 'Modificado',
        null = True,
        blank = True   
    )
    fecha = models.DateField(
        editable = False, 
        verbose_name = "Fecha de publicacion"
        )
    id_comentario = models.ForeignKey(
        'self',
        on_delete = models.CASCADE,
        related_name = 'comentario_comentado',
        null = True,
        blank = True        
        )
    imagen = models.ImageField(
        upload_to="media/images/", 
        default = None
        )
    
    def __str__(self) -> str:
        return self.contenido
    
    def save(self, *args, **kwargs):
        if self.id:
            self.modificado = datetime.utcnow()
        if (self.id_comentario is None) ^ (self.articulo is None):
            self.fecha = datetime.utcnow()
            super(Comentario, self).save(*args, **kwargs)        
        else:
            raise Exception("Debe ingresar una clave al menos y solo una")
