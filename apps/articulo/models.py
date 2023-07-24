from django.db import models
from django.urls import reverse_lazy
from django.db.models import Count

from datetime import datetime
from time import strftime



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
    is_active = models.BooleanField(
        default=True,
        verbose_name="activo"
    )
    def __str__(self) -> str:
        return str(self.nombre)

# ARTICULO
class Articulo(models.Model):
    fecha = models.DateField(editable = False,
                             verbose_name = "Fecha de publicacion"
                             )
    modificado = models.DateField(editable = False,
                                  verbose_name = 'Modificado', 
                                  null = True,
                                  blank = True
                                  )
    titulo = models.CharField(max_length=100,
                              verbose_name="Titulo",
                              )
    resumen = models.TextField(verbose_name= 'Resumen',
                               )
    contenido = models.TextField(verbose_name= "Contenido",
                                 )
    categoria = models.ForeignKey(Categoria,on_delete = models.CASCADE,
                                  null=True, 
                                  verbose_name="Categoria",
                                  )
    imagen = models.ImageField(upload_to="articulo/",
                               default = "../static/default-articulo.jpg",
                               null=True,
                               blank=True
                               )
    is_active = models.BooleanField(default=True)
    creado_por = models.ForeignKey(Usuario,
                                   on_delete = models.SET_NULL,
                                   null=True,blank=True,
                                   verbose_name="creador"
                                   )    
    
    class Meta:
        ordering = ('-fecha',)
    
    def save(self, *args, **kwargs):
        if self.id:
            self.modificado = datetime.now()
        else:
            self.fecha = datetime.now()
        super(Articulo, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("articulo:mostrarArticulo", kwargs={"id": self.pk})
        
    def get_articulos_recientes():
        ultimos_cinco_ascendente = Articulo.objects.order_by('-fecha','-id')[:5]
        return ultimos_cinco_ascendente
    
    def get_articulos_mas_comentados():
        mas_comentados = Articulo.objects.all() \
                .annotate(num_comentarios=Count('comentario')) \
                .order_by('-num_comentarios')[:5]
        return mas_comentados
        
    def get_comentario_url(self):
        return reverse_lazy("articulo:comentar", args=[self.pk])

    def get_url(self):
        return reverse_lazy("articulo_resumido", args=[self.pk])
    
    def __str__(self) -> str:
        return str(self.titulo + " " + self.fecha.strftime("%d-%m-%Y"))
    

