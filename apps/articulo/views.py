from django.shortcuts import render, redirect
from django.views.generic import DeleteView
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import UpdateView
from django.contrib import messages

from .models import Articulo, Categoria
from apps.comentario.models import Comentario
from .forms import ArticuloForm
from apps.comentario.forms import ComentarioCreationForm

# ##Vista basada en clases
class DeleteArticulo(DeleteView):
    model = Articulo
    template_name = "articulo/eliminarArticulo.html"
    def get_success_url(self):
        return reverse('articulo:articulos')

class ArticuloView(View):
    template_name = 'articulo/articulo.html'

    def get(self, request, categoria=None):
        if categoria:
            articulos = Articulo.objects.filter(categoria__nombre=categoria)
        else:
            articulos = Articulo.objects.all()
        categorias = Categoria.objects.all()
        return render(request, 'articulo/articulo.html',{'articulos' : articulos,'categorias': categorias}) ##

def articulo_crear(request):
    if request.method == "POST":
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.instance.usuario = request.user
            form.save(commit=True)
            messages.success(request, "Articulo creado correctamente")
            return redirect(reverse_lazy('articulo:articulos'))
    else:
        form = ArticuloForm()
    return render(request, 'articulo/articulo_form.html', {'form':form})

    
class ActualizarArticulo(UpdateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'articulo/articulo_form.html'
    success_url = ''

    def post(self, request, *args, **kwargs):
        messages.success(request, "Articulo actualizado correctamente")
        return super().post(request, *args, **kwargs)

class ArticuloIndividualView(View):
    def get(self, request, pk):
        articulo = Articulo.objects.filter(is_active = True).get(id=pk)
        comentarios = Comentario.objects.filter(is_active = True, articulo = articulo)
        categorias = Categoria.objects.all()
        cant_comentarios = comentarios.count()
        form = ComentarioCreationForm()
        context = { 
                'articulo' : articulo,
                'cant_comentarios' : cant_comentarios,
                'comentarios' : comentarios,
                'categorias' : categorias,
                'form' : form,
                   }
        return render(request, 'articulo/articulo_individual.html', context)

class ArticuloResumidoView(View):
    def get(self, request, id):
        articulo = Articulo.objects.get(id=id)
        categorias = Categoria.objects.all()
        context = { 
                'articulo' : articulo,
                'categorias' : categorias
                   }
        return render(request, 'articulo/articulo_resumen.html', context)
