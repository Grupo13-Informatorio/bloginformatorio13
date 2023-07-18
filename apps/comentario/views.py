from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from apps.articulo.models import Articulo

from apps.comentario.forms import ComentarioCreationForm

# Create your views here.
class RegistrarComentario(CreateView):
    form_class = ComentarioCreationForm
    template_name = 'articulo-mostrar.html'
    success_url = ('inicio')

    def form_valid(self, form, id):
        if form.is_valid():
            response_form = super().form_valid(form)
            comentario = form.save(commit=False)
            id_articulo = Articulo.objects.get(id=id)
            usuario = self.request.user
            comentario.creado_por = usuario
            comentario.articulo = Articulo.objects.get(id=id_articulo)
            comentario.save()
            return response_form
        else:
            print("estoy aca")
            form.is_invalid(form)
