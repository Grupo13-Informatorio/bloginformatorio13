from datetime import datetime
from time import strftime
from django.db import models
from django.urls import reverse_lazy

from apps.usuario.models import Usuario


# Create your models here.
# CATEGORIA
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
    activo = models.BooleanField(
        default=True,
        verbose_name="activo"
    )
    def __str__(self) -> str:
        return str(self.nombre)

# ARTICULO
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
    imagen = models.ImageField(
        upload_to="media/articulo", 
        default = "static/default-articulo.jpg",
        null=True,
        blank=True
        )
    activo = models.BooleanField(
        default=True,
        verbose_name="activo"
    )
    # creado_por = models.ForeignKey(
    #     Usuario,
    #     on_delete = models.CASCADE,
    #     editable=False,
    #     null=False,
    #     blank=False
    # )    
    
    class Meta:
        ordering = ('-fecha',)
    
    def save(self, *args, **kwargs):
        if self.id:
            self.modificado = datetime.now()
        else:
            self.fecha = datetime.now()
        super(Articulo, self).save(*args, **kwargs)
    
    def get_articulos_recientes():
        ultimos_cinco_ascendente = Articulo.objects.order_by('-fecha','-id')[:5]
        return ultimos_cinco_ascendente
    
    def get_url(self):
        return reverse_lazy("articulo_resumido", args=[self.pk])
    
    
    def __str__(self) -> str:
        return str(self.titulo + " " + self.fecha.strftime("%d-%m-%Y"))
    

