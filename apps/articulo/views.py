from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from .models import Articulo, Categoria

# Create your views here.

# class ArticulosView(View):
#     def get(self, request):
#         articulos = Articulo.objects.all()
#         return render(request, 'articulos.html', {
#             'articulos' : articulos
#         })
        
class ArticuloView(View):
    def get(self, request, id):
        articulo = Articulo.objects.get(id=id)
        context = {'articulo' : articulo}
        context.update(ArticulosView.context)
        return render(request, 'articulo.html', context)
        
# # reverse_lazy('noticias:megusta', args=[self.pk])     
   
# class ArticuloPorCategoria(View):
#     def get(self, request, id_categoria):
#         articulos = Articulo.objects.filter(categoria = id_categoria)
#         categoria = Categoria.objects.get(id=id_categoria)
#         return render(request,'articulosporcategoria.html', {
#             'articulos' : articulos,
#             'categoria' : categoria
#         })
        
# class CategoriasView(View):
#     def get(self, request):
#         categorias = Categoria.objects.all()
#         return render(request,'categorias.html', {
#             'categorias' : categorias
#         })
        
class ArticulosView(View):
    articulos = Articulo.objects.all()
    comentarios = 25
    id_usuario = "Admin"
    context = {
        'articulos' : articulos,
        'id_usuario' : id_usuario,
        'comentarios' : comentarios
        }
    def get(self, request):
        return render(request,'index.html', self.context)
