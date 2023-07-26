from django.urls import  path

from apps.usuario.views import LoginUsuario, LogoutUsuario, UpdateUsuarioView, registrarUsuario


app_name = 'usuario'

urlpatterns = [
    path('usuario/registro/',registrarUsuario.as_view(), name = 'registro'),
    path('usuario/login/', LoginUsuario.as_view(), name='login'),
    path('usuario/logout/', LogoutUsuario.as_view(), name='logout'),
    path('usuario/<int:pk>/actualizar', UpdateUsuarioView.as_view(), name="actualizar"),
]