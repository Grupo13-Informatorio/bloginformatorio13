from time import strftime
from django.db import models

# Create your models here.

class Genero(models.Model):
    nombre = models.CharField(
        max_length=35, 
        verbose_name="Genero", 
        help_text="Nombre del genero"
        )
    padre = models.ForeignKey(
        'self', 
        related_name = 'Genero_padre',
        on_delete = models.CASCADE,
        null = True,
        blank=True
        )
    
    def __str__(self) -> str:
        return str(self.nombre)


class Articulo(models.Model):
    fecha = models.DateField(auto_now = True, verbose_name = "Fecha de publicacion")
    titulo = models.CharField(max_length=100, verbose_name="Titulo", help_text="Ingrese el titulo del articulo")
    resumen = models.TextField(verbose_name= 'Resumen', help_text='Ingrese aqui su resumen')
    contenido = models.TextField(verbose_name= "Contenido", help_text="Ingrese aqui el contenido del articulo")
    genero = models.ForeignKey(Genero, on_delete = models.CASCADE, null=True, verbose_name="Genero", help_text="Ingrese el genero")
    
    
    
    def __str__(self) -> str:
        return str(self.titulo + " " + self.fecha.strftime("%d-%m-%Y"))
    

