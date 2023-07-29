from django.urls import path

from apps.contacto.views import ContactoUsuario, DetalleContactoView, ListarContactosView

app_name = 'contacto'

urlpatterns = [
    path('contacto/', ContactoUsuario.as_view(), name='contacto'),
    path('contactos/ver/', ListarContactosView.as_view(), name='verContactos'),
    path('contacto/<int:pk>/ver', DetalleContactoView.as_view(), name='detalle'),
]