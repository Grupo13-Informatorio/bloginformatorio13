from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Comentario
from .forms import ComentarioForm
from django.views.generic import DeleteView
from apps.usuario.models import Usuario
from django.urls import reverse
from apps.articulo.models import Articulo

@login_required
def comentar(request,id):
    articulo = get_object_or_404(Articulo, id=id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.articulo = articulo
            comentario.usuario = request.user
            comentario.save()
            return redirect('leer_articulo', id=id)
    else:
        form = ComentarioForm()
    return render(request, 'comentario/comentar.html',{'form': form, 'articulo': articulo})

def listado_comentario(request):
    comentarios = Comentario.objects.all()
    usuario = request.user.id

    context={
        'comentarios': comentarios,
        'usuario': usuario,
    }
    return render(request, 'comentario/listadoComentario.html', context)

def agregarComentario(request):
    usuario = Usuario(usuario = request.user)
    form = Comentario(request.POST or None)
    if form.is_valid():
        form.save()
        form = ComentarioForm()
        
    context={
        'form': form,
        'usuario': usuario,
    }
    return render(request, 'comentario/agregarComentario.html', context)


class DeleteComentario(DeleteView):
    model = Comentario
    template_name = "comentario/eliminarComentario.html"
    def get_success_url(self):
        return reverse('apps.articulo:articulos')

def detalle_articulo(request, articulo_id):
    articulo = Articulo.objects.get(id=articulo_id)
    comentarios= Comentario.objects.filter(articulo=articulo)
    return render(request, 'detalle_articulo.html', {'articulo': articulo,'comentarios': comentarios})