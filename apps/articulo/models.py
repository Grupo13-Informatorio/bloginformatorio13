from datetime import datetime
from time import strftime
from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(
        max_length=35, 
        verbose_name="categoria", 
        help_text="Nombre de la categoria")
    padre = models.ForeignKey(
        'self', 
        related_name = 'categoria_padre',
        on_delete = models.CASCADE,
        null = True,
        blank=True)
    
    def __str__(self) -> str:
        return str(self.nombre)

class Articulo(models.Model):
    fecha = models.DateField(
        editable = False, 
        verbose_name = "Fecha de publicacion"
        )
    modificado = models.DateField(
        editable = True,
        verbose_name = 'Modificado',
        null = True,
        blank = True   
    )
    titulo = models.CharField(
        max_length=100, 
        verbose_name="Titulo", 
        help_text="Ingrese el titulo del articulo"
        )
    resumen = models.TextField(
        verbose_name= 'Resumen', 
        help_text='Ingrese aqui su resumen'
        )
    contenido = models.TextField(
        verbose_name= "Contenido", 
        help_text="Ingrese aqui el contenido del articulo"
        )
    categoria = models.ForeignKey(
        Categoria, 
        on_delete = models.CASCADE, 
        null=True, 
        verbose_name="Categoria", 
        help_text="Ingrese la categoria"
        )
    imagen = models.ImageField(
        upload_to="media/images/", 
        default = None
        )
    
    def save(self, *args, **kwargs):
        if self.id:
            self.modificado = datetime.utcnow()
        else:
            self.fecha = datetime.utcnow()
        super(Articulo, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return str(self.titulo + " " + self.fecha.strftime("%d-%m-%Y"))
    

