from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import View

from apps.comentario.models import Comentario

from .models import Articulo

# Create your views here.


class ArticuloView(View):
    def get(self, request, id):
        articulo = Articulo.objects.get(id=id)
        comentarios = Comentario.objects.filter(articulo=articulo)
        cant_comentarios = comentarios.count()
        id_usuario = "Admin"
        context = { 
                'articulo' : articulo,
                'id_usuario' : id_usuario,
                'cant_comentarios' : cant_comentarios,
                'comentarios' : comentarios
                   }
        return render(request, 'articulo_mostrar.html', context)
        

class ArticulosView(View):
    def get(self, request):
        articulos_banner = Articulo.get_articulos_recientes()
        articulos = Articulo.objects.all()
        id_usuario = "Admin"
        context = { 
                'articulos_banner' : articulos_banner,
                'articulos' : articulos,
                'id_usuario' : id_usuario,
                   }
        return render(request, 'articulos_todos.html', context)


class ArticuloResumidoView(View):
    def get(self, request, id):
        articulo = Articulo.objects.get(id=id)
        context = { 
                'articulo' : articulo,
                'id_usuario' : "Admin",
                'comentarios' : 35
                   }
        return render(request, 'articulo_resumen.html', context)