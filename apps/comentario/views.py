from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from apps.articulo.models import Articulo

from apps.comentario.forms import ComentarioCreationForm

# Create your views here.
class registrarComentario(CreateView):
    template_name = 'form-comentarios.html'
    form_class = ComentarioCreationForm
    success_url = reverse_lazy('registration_success')
    
    def form_valid(self, form, id):
        if form.is_valid():
            response_form = super().form_valid(form)
            comentario = form.save(commit=False)
            usuario = self.request.user
            comentario.usuario = usuario
            comentario.articulo = Articulo.objects.get(id=id)
            comentario.save()
            return response_form
        else:
            form.is_invalid(form)
