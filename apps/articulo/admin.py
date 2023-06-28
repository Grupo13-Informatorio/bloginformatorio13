from django.contrib import admin

from apps.articulo.models import Articulo, Genero

# Register your models here.


class GeneroModel(admin.ModelAdmin):
    list_display = ('nombre', 'padre')

class ArticuloModel(admin.ModelAdmin):
    list_display = ('fecha', 'titulo','resumen', 'contenido', 'genero')

admin.site.register(Articulo, ArticuloModel)
admin.site.register(Genero, GeneroModel)