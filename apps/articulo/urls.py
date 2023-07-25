from django.urls import  path

from apps.comentario.views import  registrarComentario
from .views import  ArticuloBusquedaView, ArticuloListView, ArticuloResumidoView, CategoriaListView, ArticuloView,  CrearArticulo, EditarArticulo

app_name = 'articulo'

urlpatterns = [
    path('articulos/', ArticuloListView.as_view(), name='articulos'),
    path('articulo/<int:id>/',ArticuloView.as_view(), name='mostrarArticulo'),
    path('articulo/crear/',CrearArticulo.as_view(), name='crear'),
    path('articulo_resumido/<int:id>/',ArticuloResumidoView.as_view(), name='articulo_resumido'),
    path('articulo/<int:id>/comentar/', registrarComentario, name='comentar'),
    path('articulo/<int:pk>/editar/', EditarArticulo.as_view(), name='editar'),
    path('categoria/<int:pk>/', CategoriaListView.as_view(), name='categoria'),
    path('articulo/buscar/',ArticuloBusquedaView.as_view(), name='buscar'),
]