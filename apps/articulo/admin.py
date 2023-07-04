from django.contrib import admin
from .models import Categoria, Articulo

# Register your models here.

@admin.register(Articulo)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','titulo', 'resumen','contenido','fecha_hora','imagen','estado','categoria','publicado')

admin.site.register(Categoria)