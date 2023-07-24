from django.shortcuts import render
from django.views import View

from apps.articulo.models import Articulo, Categoria


class IndexView(View):
    def get(self, request):
        articulos_banner = Articulo.get_articulos_mas_comentados()
        articulos = Articulo.objects.all().filter(is_active=True).order_by('-fecha','-id')[:5]
        categorias = Categoria.objects.all()
        context = { 
                'articulos_banner' : articulos_banner,
                'articulos' : articulos,
                'categorias' : categorias
                   }
        return render(request, 'index.html', context)

def contacto(request):
    return render(request,'contacto/contacto.html')

def sobre_nosotros(request):
    return render(request, 'nosotros.html')

def registration_success(request):
    return render(request,'registration/registration_success.html' )

