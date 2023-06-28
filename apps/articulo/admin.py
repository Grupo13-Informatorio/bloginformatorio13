from django.contrib import admin

from apps.articulo.models import Articulo, Genero

# Register your models here.


class GeneroModel(admin.ModelAdmin):
    list_display = ('nombre', 'padre')
    

admin.site.register(Articulo)
admin.site.register(Genero, GeneroModel)