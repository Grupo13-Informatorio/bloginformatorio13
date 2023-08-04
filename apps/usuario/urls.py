from django.urls import  path
from django.contrib.auth.decorators import permission_required
from apps.usuario.views import CambiarEstadoView, CambiarRolView, LoginUsuario, LogoutUsuario, UpdateUsuarioView, VerUsuariosView, registrarUsuario, VerPerfilUsuario


app_name = 'usuario'

urlpatterns = [
    path('usuario/registro/', registrarUsuario.as_view(), name = 'registro'),
    path('usuario/login/', LoginUsuario.as_view(), name='login'),
    path('usuario/logout/', LogoutUsuario.as_view(), name='logout'),
    path('usuario/<int:pk>/actualizar/', UpdateUsuarioView.as_view(), name="actualizar"),
    path('usuario/<int:pk>/ver_perfil/', VerPerfilUsuario.as_view(), name="perfil"),
    path('usuario/usuarios/', VerUsuariosView.as_view(), name="usuarios"),
    path('usuario/estado/<int:pk>', CambiarEstadoView.as_view(), name="cambiar_estado"),
    path('usuario/cambiarrol/<int:pk>', CambiarRolView.as_view(), name="cambiar_rol"),
]