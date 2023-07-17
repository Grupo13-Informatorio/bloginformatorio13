from django.urls import  path
from .views import  registrarComentario


app_name = 'comentario'

urlpatterns = [
    path('/comentar',registrarComentario.as_view(), name = 'comentario'),
]