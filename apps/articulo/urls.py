from django.urls import path
from .views import ArticuloView ##Este articulos o ArticuloView(vista por clases) hace referencia al de view.py de la app articulo
from . import views

app_name = 'apps.articulo'

urlpatterns = [
    path('articulos/', ArticuloView.as_view(), name='articulos'),
    path('leer_articulo/<int:id>', views.leer_articulo, name="leer_articulo"),
    path('articulo_actualizar/<int:id>', views.articulo_actualizar, name="articulo_actualizar"),
    path('eliminarArticulo/<pk>', views.DeleteArticulo.as_view(), name='eliminarArticulo'),
]