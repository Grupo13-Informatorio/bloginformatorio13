from django.urls import  path
from .views import  ArticuloView, ArticulosView

urlpatterns = [
    path('articulos/',ArticulosView.as_view(), name = 'articulos'),
    path('articulo/<int:id>',ArticuloView.as_view(), name = 'mostrarArticulo'),
    # path('categoria/<int:id_categoria>',ArticuloPorCategoria.as_view(), name = 'articulosPorCategoria'),
    # path('categorias/',CategoriasView.as_view(), name = 'categorias'),
]