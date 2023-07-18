from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from apps.articulo.models import Articulo

from apps.comentario.forms import ComentarioCreationForm

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