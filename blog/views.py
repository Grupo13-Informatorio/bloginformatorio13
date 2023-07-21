from django.views import View
from django.shortcuts import render

from apps.articulo.models import Articulo
##Si quiero activar esta vista basada en funciones importar from django.shortcuts import render y tambien se usa en clase porque o sino se rompe 
# def index(request):
#     return render(request, 'index.html')



##CUANDO QUIERA CAMBIAR AL ESTILO DE CLASE ACTIVAR LAS LINEAS DE ABAJO y el (# from .views import IndexView) del urls.py de blog cambiando la linea 25 de index a IndexView.as_view()
##Tambien si activo esto render ya no me sirve porque estoy usando una templateview
class IndexView(View):
    def get(self, request):
        context = {
            'articulos': Articulo.objects.order_by('-fecha_hora')[:5],
            'home': Articulo.objects.order_by('-fecha_hora')[:5],
        }
        return render(request, 'index.html', context) #contexto son los valores a traves de los cuales voy a llamar a la plantilla para tal o cual cosa
    
class AboutView(View):
    def get(self, request):
        return render(request,'sobrenosotros.html')
    
class ContactenosView(View):
    def get(self,request):
        return render(request,'contactenos.html')
    