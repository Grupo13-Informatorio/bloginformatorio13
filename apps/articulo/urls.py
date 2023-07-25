from django.urls import path
from .views import ArticuloView 
from . import views

app_name = 'apps.articulo'

urlpatterns = [
    path('articulos/', ArticuloView.as_view(), name='articulos'),
    path('leer_articulo/<int:id>', views.leer_articulo, name="leer_articulo"),
    path('articulo_actualizar/<int:pk>/', views.articulo_actualizar, name="articulo_actualizar"),
    path('articulo_crear/', views.articulo_crear, name="articulo_crear"),
    path('eliminarArticulo/<int:pk>/', views.DeleteArticulo.as_view(), name='eliminarArticulo'),
]