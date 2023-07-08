from datetime import datetime
from time import strftime
from django.db import models
from django.urls import reverse_lazy
from django_resized import ResizedImageField

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
        editable = False,
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
    imagen = ResizedImageField(
        size=[1024, 768],
        upload_to="media/articulo", 
        default = "static/default-articulo.jpg",
        crop = ['middle', 'center'],
        null=True,
        blank=True
        )
    
    imagen_carrusel = ResizedImageField(
        
        size=[640, 480],
        upload_to="media/articulo/carrusel", 
        default = "static/default-articulo.jpg",
        crop = ['middle', 'center'],
        null=True,
        blank=True
        )
    
    class Meta:
        ordering = ('-fecha',)
    
    def save(self, *args, **kwargs):
        if self.id:
            self.modificado = datetime.now()
        else:
            self.fecha = datetime.now()
        # ACA DEJO PARA SEGUIR EL LUNES self.imagen_carrusel = 
        super(Articulo, self).save(*args, **kwargs)
    
    def get_articulos_recientes():
        ultimos_cinco = Articulo.objects.order_by('-fecha')[:5]
        ultimos_cinco_ascendente = reversed(ultimos_cinco)
        return ultimos_cinco_ascendente
    
    def get_url(self, **kwargs):
        return reverse_lazy("articulo_resumido", args=[self.pk])
    
    
    def __str__(self) -> str:
        return str(self.titulo + " " + self.fecha.strftime("%d-%m-%Y"))
    

