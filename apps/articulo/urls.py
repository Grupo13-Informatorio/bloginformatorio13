from django.urls import  path

from apps.comentario.views import RegistrarComentario
from .views import  ArticuloResumidoView, ArticuloView, ArticulosView

app_name = 'articulo'

urlpatterns = [
    path('articulos/',ArticulosView.as_view(), name = 'articulos'),
    path('articulo/<int:id>',ArticuloView.as_view(), name = 'mostrarArticulo'),
    path('articulo_resumido/<int:id>',ArticuloResumidoView.as_view(), name = 'articulo_resumido'),
    path('articulo/<int:id>/comentar', RegistrarComentario.as_view(), name='comentar')
]