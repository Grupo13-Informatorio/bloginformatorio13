from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone

from apps.usuario.models import Usuario

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    is_active = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.nombre


class Articulo(models.Model):
    titulo = models.CharField(max_length=30, null=False)
    resumen = models.TextField(null=False)
    contenido = models.TextField(null=False)
    imagen = models.ImageField(null=True, blank=True, upload_to='articulo', default='articulo/default_articulo.jpg')
    is_active = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='Sin categoría')
    publicado = models.DateTimeField(default=timezone.now, editable=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        ordering= ('-publicado',)

    def __str__(self):
        return self.titulo
    
    def delete(self, using = None, keep_parents = False):
        self.imagen.delete(self.imagen.name)
        super().delete()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("articulo:articulo", kwargs={"pk": self.pk})
        
    def get_articulos_recientes():
        ultimos_cinco_ascendente = Articulo.objects.order_by('-publicado','-id')[:5]
        return ultimos_cinco_ascendente
    
    def get_comentario_url(self):
        return reverse_lazy("articulo:comentar", args=[self.pk])
    
    def get_url(self):
        return reverse_lazy("articulo:resumen", args=[self.pk])
    