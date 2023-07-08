from django.shortcuts import render
from django.views import View
from apps.articulo.models import Articulo



class IndexView(View):
    def get(self, request):
        articulos_banner = Articulo.get_articulos_recientes()
        articulos = Articulo.objects.all()
        comentarios = 25
        id_usuario = "Admin"
        context = { 
                'articulos_banner' : articulos_banner,
                'articulos' : articulos,
                'id_usuario' : id_usuario,
                'comentarios' : comentarios
                   }
        return render(request, 'index.html', context)

def contacto(request):
    return render(request,'contacto.html')

def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')