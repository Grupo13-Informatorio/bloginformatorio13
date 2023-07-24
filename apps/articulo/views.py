from typing import Any, Dict
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import UpdateView
from django.views.generic import CreateView, ListView
from django.contrib import messages

from apps.articulo.forms import ArticuloCreationForm
from apps.comentario.forms import ComentarioCreationForm
from apps.comentario.models import Comentario

from .models import Articulo, Categoria

# Create your views here.

class ArticuloView(View):
    def get(self, request, id):
        articulo = Articulo.objects.filter(is_active = True).get(id=id)
        articulos = Articulo.objects.filter(is_active = True).order_by('-fecha','-id')[:5]
        comentarios = Comentario.objects.filter(is_active = True, articulo = articulo)
        categorias = Categoria.objects.all()
        cant_comentarios = comentarios.count()
        form = ComentarioCreationForm()
        context = { 
                'articulos_banner' : articulos,
                'articulo' : articulo,
                'cant_comentarios' : cant_comentarios,
                'comentarios' : comentarios,
                'categorias' : categorias,
                'form' : form,
                   }
        return render(request, 'articulo/articulo_mostrar.html', context)
        
# class ArticulosView(View):
#     def get(self, request):
#         articulos_banner = Articulo.get_articulos_recientes()
#         articulos = Articulo.objects.all()
#         categorias = Categoria.objects.all()
#         context = { 
#                 'articulos_banner' : articulos_banner,
#                 'articulos' : articulos,
#                 'categorias' : categorias
#                    }
#         return render(request, 'articulo/articulos_todos.html', context)

class ArticuloResumidoView(View):
    def get(self, request, id):
        articulo = Articulo.objects.get(id=id)
        categorias = Categoria.objects.all()
        context = { 
                'articulo' : articulo,
                'categorias' : categorias
                   }
        return render(request, 'articulo/articulo_resumen.html', context)


class EditarArticulo(UpdateView):
    
    model = Articulo
    form_class = ArticuloCreationForm
    template_name = 'articulo/articulo_editar.html'
    success_url = ''
    def post(self, request: HttpRequest, *args: str, **kwargs: Any):
        messages.success(request, "Articulo actualizado correctamente")
        return super().post(request, *args, **kwargs)
    
class CrearArticulo(CreateView):
    
    form_class = ArticuloCreationForm
    template_name = 'articulo/articulo_crear.html'
    
    def form_valid(self, form):
        if form.is_valid:
            form.instance.creado_por = self.request.user
            messages.success(self.request, "Articulo creado exitosamente")
            return super().form_valid(form)
        else:
            messages.error(self.request, "Error en la validacion")
            return render(self.request, 'articulo/articulo_crear.html', {'form': form})
        
class ArticuloListVieww(ListView):
    model = Articulo
    paginate_by = 4
    template_name = 'articulo/articulos_todos.html'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['articulos_banner'] = Articulo.get_articulos_mas_comentados()
        context['categorias'] = Categoria.objects.all()
        return context
    
    def get_queryset(self):
        articulos = Articulo.objects.filter(is_active=True).order_by('-fecha')
        return articulos
        

class ArticuloPorCategoriaListVieww(ListView):
    model = Articulo
    paginate_by = 4
    template_name = 'articulo/articulos_todos.html'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['articulos_banner'] = Articulo.get_articulos_mas_comentados()
        context['categorias'] = Categoria.objects.all()
        return context
    
    def get_queryset(self):
        articulos = Articulo.objects \
                .filter(is_active=True, categoria=Categoria.objects.get(pk=self.request.GET.get('categoria'))) \
                .order_by('-fecha')
        return articulos
        
   
