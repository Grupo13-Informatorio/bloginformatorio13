from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from apps.articulo.models import Articulo

from apps.comentario.forms import ComentarioCreationForm
from apps.comentario.models import Comentario

def registrarComentario(request, id):
    if request.method == "POST":
        form = ComentarioCreationForm(data = request.POST)
        form.instance.creado_por = request.user
        articulo = Articulo.objects.get(id=id)
        form.instance.articulo = articulo
        if form.is_valid():
            form.save()
        else:
            return redirect('articulo:mostrarArticulo', id)
    return redirect('articulo:mostrarArticulo', id)


def registrarRespuestaAComentario(request, id):
    if request.method == "POST": 
        comentario_id = request.POST.get('comentario')
        comentario = Comentario.objects.get(id=comentario_id)
        contenido = request.POST.get('contenido')
        usuario = request.user
        nuevo_comentario = Comentario()
        nuevo_comentario.comentario_padre = comentario
        nuevo_comentario.creado_por = usuario
        nuevo_comentario.contenido = contenido
        nuevo_comentario.save()
    return redirect('articulo:mostrarArticulo', id)
    