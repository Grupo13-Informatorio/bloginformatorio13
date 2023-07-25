from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from apps.articulo.models import Articulo, Categoria


class IndexView(View):
    def get(self, request):
        articulos_banner = Articulo.get_articulos_recientes()
        articulos = Articulo.objects.all()
        categorias = Categoria.objects.all()
        context = { 
                'articulos_banner' : articulos_banner,
                'articulos' : articulos,
                'categorias' : categorias
                   }
        return render(request, 'index.html', context)



def sobre_nosotros(request):
    return render(request, 'nosotros.html')

   
def registration_success(request):
    return render(request,'registration/registration_success.html' )

