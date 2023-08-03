from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages


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


class EditarComentario(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Comentario
    form_class = ComentarioCreationForm
    template_name = 'comentario/comentario_editar.html'
    success_url = ''


    def test_func(self):
        if (self.request.user.is_miembro or self.request.user.is_superuser or self.get_object().creado_por == self.request.user):
            return True
        else:
            return False

    def post(self, request, *args, **kwargs):
        self.success_url = request.GET.get('next')
        messages.success(request, "Articulo actualizado correctamente")
        return super().post(request, *args, **kwargs)

class BorrarComentarioView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Comentario
    template_name = 'comentario/comentario_borrar.html'
    success_url = ''

    def test_func(self):
        if (self.request.user.is_miembro or self.request.user.is_superuser or self.get_object().creado_por == self.request.user):
            return True
        else:
            return False

    def get_success_url(self) -> str:
        self.success_url = self.request.GET.get('next')
        messages.success(self.request, "Comentario borrado exitosamente")
        return super().get_success_url()
