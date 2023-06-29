from django.contrib import admin

from apps.articulo.models import Articulo, Categoria

# Register your models here.


class CategoriaModel(admin.ModelAdmin):
    list_display = ('nombre', 'padre')

class ArticuloModel(admin.ModelAdmin):
    list_display = ('fecha', 'titulo','resumen', 'contenido', 'categoria')

admin.site.register(Articulo, ArticuloModel)
admin.site.register(Categoria, CategoriaModel)