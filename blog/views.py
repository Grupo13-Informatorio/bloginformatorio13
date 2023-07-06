from django.shortcuts import render

from apps.articulo.views import ArticulosView


def index(request):
    return render(request,'index.html', ArticulosView.context)

def contacto(request):
    return render(request,'contacto.html')

def sobre_nosotros(request):
    return render(request, 'index.html')