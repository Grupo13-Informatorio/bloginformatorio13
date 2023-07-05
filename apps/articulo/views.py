from django.shortcuts import render
from .models import Articulo
## para llamar a clase utilizar el comando de abajo
from django.views import View

#vista bassada en funcion
# def articulos(request):
#     articulos = Articulo.objects.all()
#     return render(request, 'articulo.html',{'articulos' : articulos})

# ##Vista basada en clases

class ArticuloView(View):
    template_name = 'articulo.html'

    def get(self, request):
        articulos = Articulo.objects.all()
        return render(request, 'articulo.html',{'articulos' : articulos})
