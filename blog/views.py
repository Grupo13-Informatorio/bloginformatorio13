from django.views import View
from django.shortcuts import render
##Si quiero activar esta vista basada en funciones importar from django.shortcuts import render y tambien se usa en clase porque o sino se rompe 
# def index(request):
#     return render(request, 'index.html')



##CUANDO QUIERA CAMBIAR AL ESTILO DE CLASE ACTIVAR LAS LINEAS DE ABAJO y el (# from .views import IndexView) del urls.py de blog cambiando la linea 25 de index a IndexView.as_view()
##Tambien si activo esto render ya no me sirve porque estoy usando una templateview
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')