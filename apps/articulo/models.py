from django.db import models
from django.utils import timezone

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=30, null=False)


class Articulo(models.Model):
    '''
    Clase: Articulo
    Hereda de: objeto
    Atributos de clase: id, articulos (lista)
    Atributos en constructor: id_usuario, titulo, resumen, contenido
    Atributos por defecto: id = autogenerado, fecha_hora = fecha y hora actual, estado = True
    Propiedades: fecha
    Metodos de clase: __generar_id
    Metodos de instancia: set_estado
    Metodo __str__ devuelve "ID - Titulo - Resumen - Usuario - Activo"
    '''
    
    #self.id_usuario = id_usuario
    titulo = models.CharField(max_length=30, null=False)
    resumen = models.TextField(null=False)
    contenido = models.TextField(null=False)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='media/articulo/', default='media/articulo/default_articulo.jpg')
    estado = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='Sin categoría')
    publicado = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering= ('-publicado',)

    def __str__(self):
        return self.titulo
    
    def delete(self, using = None, keep_parents = False):
        self.imagen.delete(self.imagen.name)
        super().delete()


    # def __generar_id():
    #     '''Devuelve ID distinto en cada instancia'''
    #     actual = Articulo.id
    #     Articulo.id += 1
    #     return actual
    
    # def get_fecha_hora(self):
    #     return self.fecha_hora
    
    # fecha = property(get_fecha_hora)
    
    # def set_estado(self, estado):
    #     self.estado = bool(estado)
    
    # def __repr__(self) -> str:
    #     return f"ID {self.id} - {self.fecha_hora} - Titulo:{self.titulo} - Resumen:{self.resumen} - Usuario:{self.id_usuario} - Activo:{self.estado}"