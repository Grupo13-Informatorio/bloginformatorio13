from typing import Optional
from django.http import HttpRequest 
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import CreateView, ListView
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from apps.articulo.forms import ArticuloCreationForm, CategoriaForm
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
   
   
        
class ArticuloResumidoView(View):
    def get(self, request, id):
        articulo = Articulo.objects.get(id=id)
        categorias = Categoria.objects.all()
        context = { 
                'articulo' : articulo,
                'categorias' : categorias
                   }
        return render(request, 'articulo/articulo_resumen.html', context)



class EditarArticulo(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    
    def test_func(self):
        if (self.request.user.is_miembro or self.request.user.is_superuser):
            return True
        else:
            return False
    
    model = Articulo
    form_class = ArticuloCreationForm
    template_name = 'articulo/articulo_editar.html'
    success_url = ''
    def post(self, request, *args, **kwargs):
        messages.success(request, "Articulo actualizado correctamente")
        return super().post(request, *args, **kwargs)



class CrearArticulo(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    

    form_class = ArticuloCreationForm
    template_name = 'articulo/articulo_crear.html'
    
    def test_func(self):
        if (self.request.user.is_miembro or self.request.user.is_superuser):
            return True
        else:
            return False
    
    def form_valid(self, form):
        if form.is_valid:
            form.instance.creado_por = self.request.user
            messages.success(self.request, "Articulo creado exitosamente")
            return super().form_valid(form)
        else:
            messages.error(self.request, "Error en la validacion")
            return render(self.request, 'articulo/articulo_crear.html', {'form': form})



class ArticuloListView(ListView):
    
    model = Articulo
    paginate_by = 4
    template_name = 'articulo/articulos_todos.html'
    cantidad_registros = 0
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articulos_banner'] = Articulo.get_articulos_mas_comentados()
        context['categorias'] = Categoria.objects.all()
        context['registros'] = self.cantidad_registros
        return context
    
    def get_queryset(self):
        articulos = Articulo.objects.filter(is_active=True).order_by('-fecha')
        self.cantidad_registros = articulos.count()
        return articulos



class CategoriaListView(ListView):
    
    model = Articulo
    paginate_by = 4
    template_name = 'articulo/articulos_todos.html'
    cantidad_registros = 0
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articulos_banner'] = Articulo.get_articulos_mas_comentados()
        context['registros'] = self.cantidad_registros
        context['categorias'] = Categoria.objects.all()
        context['categoria'] = Categoria.objects.get(id=self.kwargs['pk'])
        return context

    def get_queryset(self):
        articulos = Articulo.objects \
                .filter(is_active=True, categoria=Categoria.objects.get(id=self.kwargs['pk'])) \
                .order_by('-fecha')
        self.cantidad_registros = articulos.count()
        return articulos
        


class ArticuloBusquedaView(ListView):
    
    model = Articulo
    paginate_by = 4
    template_name = 'articulo/articulos_todos.html'
    ordering = '-fecha'
    cantidad_registros = 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['registros'] = self.cantidad_registros
        context['categorias'] = Categoria.objects.all()
        context['filter'] = self.request.GET.get('filter', '')
        context['orderby'] = self.request.GET.get('orderby', '-fecha')        
        return context

    def get_queryset(self):
        filter_val = self.request.GET.get('filter')
        order = self.request.GET.get('orderby')
        if not order:
            order = '-fecha'
        if not filter_val:
            filter_val = ''
        new_context = Articulo.objects  \
            .filter(    \
            Q(titulo__icontains=filter_val) | Q(resumen__icontains=filter_val) | Q(contenido__icontains=filter_val))    \
            .order_by(order)
        return new_context




class CrearCategoria(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    
    form_class = CategoriaForm
    template_name = 'articulo/categoria_crear.html'
     
     
    def test_func(self):
        if (self.request.user.is_miembro or self.request.user.is_superuser):
            return True
        else:
            return False
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next')
        return context    
    
    def form_valid(self, form):
        if form.is_valid:
            messages.success(self.request, "Categoria agregada exitosamente")
            self.success_url = self.request.POST.get('next') 
            return super().form_valid(form)
        else:
            messages.error(self.request, "Error en la validacion")
            return render(self.request, 'articulo/articulo_crear.html', {'form': form}) 
    
        
        
class BorrarArticuloView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    
    def test_func(self):
        if (self.request.user.is_miembro or self.request.user.is_superuser):
            return True
        else:
            return False
    
    model = Articulo
    template_name = 'articulo/articulo_borrar.html'
    success_url = reverse_lazy('articulo:articulos')
    
    def get_success_url(self) -> str:
        messages.success(self.request, "Articulo borrado exitosamente")
        return super().get_success_url()
    
   
    
class BorrarCategoriaView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    
    def test_func(self):
        if (self.request.user.is_miembro or self.request.user.is_superuser):
            return True
        else:
            return False
    
    model = Categoria
    template_name = 'articulo/categoria_borrar.html'
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['next'] = self.request.GET.get('next')
        return ctx
    
    def post(self, request: HttpRequest, *args, **kwargs):
        self.success_url = request.POST.get('next')
        return super().post(request, *args, **kwargs)
    
    def get_success_url(self) -> str:
        messages.success(self.request, "Categoria borrada exitosamente")
        return super().get_success_url()