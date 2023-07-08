from django.urls import  path
from .views import  ArticuloResumidoView, ArticuloView, ArticulosView

urlpatterns = [
    path('articulos/',ArticulosView.as_view(), name = 'articulos'),
    path('articulo/<int:id>',ArticuloView.as_view(), name = 'mostrarArticulo'),
    path('articulo_resumido/<int:id>',ArticuloResumidoView.as_view(), name = 'articulo_resumido'),
    # path('categorias/',CategoriasView.as_view(), name = 'categorias'),
]