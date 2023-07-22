from django.urls import path

from apps.comentario.views import registrarComentario
from .views import ArticuloResumidoView, ArticuloView 
from . import views

app_name = 'articulo'

urlpatterns = [
    path('articulos/', ArticuloView.as_view(), name="articulos"),
    path('articulo/<int:pk>/ver/', views.ArticuloIndividualView.as_view(), name="articulo"),
    path('articulo_resumido/<int:id>', ArticuloResumidoView.as_view(), name = 'articulo_resumido'),
    path('articulo/<int:pk>/editar/', views.ActualizarArticulo.as_view(), name="editar"),
    path('articulo/crear/', views.articulo_crear, name="crear"),
    path('articulo/<int:pk>/eliminar/', views.DeleteArticulo.as_view(), name="eliminar"),
    path('articulo/<int:id>/comentar', registrarComentario, name='comentar'),
    ]