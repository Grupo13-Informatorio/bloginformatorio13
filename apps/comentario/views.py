from typing import Any
from django.shortcuts import redirect
from apps.articulo.models import Articulo

from .forms import ComentarioCreationForm

def registrarComentario(request, id):
    if request.method == "POST":
        form = ComentarioCreationForm(data = request.POST)
        form.instance.usuario = request.user
        articulo = Articulo.objects.get(id=id)
        form.instance.articulo = articulo
        if form.is_valid():
            form.save()
        else:
            return redirect('articulo:articulo', id)
    return redirect('articulo:articulo', id)