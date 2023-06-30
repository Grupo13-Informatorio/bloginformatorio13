from django.shortcuts import render
from django.views import View

from .models import Articulo

# Create your views here.

class ArticuloView(View):
    def get(self, request):
        articulos = Articulo.objects.all()
        return render(request, 'articulo.html', {
            'articulos' : articulos
        })