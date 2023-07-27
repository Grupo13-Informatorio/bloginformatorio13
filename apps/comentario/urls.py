from django.urls import  path

from .views import  BorrarArticuloView, EditarArticulo

app_name = 'comentario'

urlpatterns = [
    path('comentario/<int:pk>/editar', EditarArticulo.as_view(), name='editar'),
    path('comentario/<int:pk>/borrar', BorrarArticuloView.as_view(), name='borrar'),
]