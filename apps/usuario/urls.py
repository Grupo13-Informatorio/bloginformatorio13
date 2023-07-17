from django.urls import  path

from apps.usuario.views import registrarUsuario


app_name = 'usuario'

urlpatterns = [
    path('usuario/registro/',registrarUsuario.as_view(), name = 'registro'),
]