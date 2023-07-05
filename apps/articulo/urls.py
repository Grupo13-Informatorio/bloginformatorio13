from django.urls import path
from .views import ArticuloView ##Este articulos hace referencia al de view.py de la app articulo


urlpatterns = [
    path('articulos/', ArticuloView.as_view(), name='articulos'),
]