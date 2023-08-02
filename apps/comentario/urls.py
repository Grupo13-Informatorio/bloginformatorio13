from django.urls import  path

from .views import  BorrarComentarioView, EditarComentario

app_name = 'comentario'

urlpatterns = [
    path('comentario/<int:pk>/editar/', EditarComentario.as_view(), name='editar'),
    path('comentario/<int:pk>/borrar/', BorrarComentarioView.as_view(), name='borrar'),
]