from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import View

from apps.comentario.models import Comentario

from .models import Articulo, Categoria

# Create your views here.


class ArticuloView(View):
    def get(self, request, id):
        articulo = Articulo.objects.get(id=id)
        comentarios = Comentario.objects.filter(articulo=articulo)
        categorias = Categoria.objects.all()
        cant_comentarios = comentarios.count()
        id_usuario = "Admin"
        context = { 
                'articulo' : articulo,
                'id_usuario' : id_usuario,
                'cant_comentarios' : cant_comentarios,
                'comentarios' : comentarios,
                'categorias' : categorias
                   }
        return render(request, 'articulo_mostrar.html', context)
        

class ArticulosView(View):
    def get(self, request):
        articulos_banner = Articulo.get_articulos_recientes()
        articulos = Articulo.objects.all()
        categorias = Categoria.objects.all()
        id_usuario = "Admin"
        context = { 
                'articulos_banner' : articulos_banner,
                'articulos' : articulos,
                'id_usuario' : id_usuario,
                'categorias' : categorias
                   }
        return render(request, 'articulos_todos.html', context)


class ArticuloResumidoView(View):
    def get(self, request, id):
        articulo = Articulo.objects.get(id=id)
        categorias = Categoria.objects.all()
        context = { 
                'articulo' : articulo,
                'id_usuario' : "Admin",
                'comentarios' : 35,
                'categorias' : categorias
                   }
        return render(request, 'articulo_resumen.html', context)