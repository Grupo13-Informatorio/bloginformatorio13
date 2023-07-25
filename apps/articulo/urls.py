from django.urls import  path

from apps.comentario.views import  registrarComentario
from .views import  ArticuloBusquedaView, ArticuloListVieww, ArticuloPorCategoriaListVieww, ArticuloResumidoView, ArticuloView,  CrearArticulo, EditarArticulo

app_name = 'articulo'

urlpatterns = [
    path('articulos/', ArticuloListVieww.as_view(), name='articulos'),
    path('articulo/<int:id>/',ArticuloView.as_view(), name='mostrarArticulo'),
    path('articulo/crear/',CrearArticulo.as_view(), name='crear'),
    path('articulo_resumido/<int:id>/',ArticuloResumidoView.as_view(), name='articulo_resumido'),
    path('articulo/<int:id>/comentar/', registrarComentario, name='comentar'),
    path('articulo/<int:pk>/editar/', EditarArticulo.as_view(), name='editar'),
    path('categoria/articulo/', ArticuloPorCategoriaListVieww.as_view(), name='categoria'),
    path('articulo/buscar/',ArticuloBusquedaView.as_view(), name='buscar'),

]