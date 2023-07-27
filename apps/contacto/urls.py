from django.urls import path

from apps.contacto.views import ContactoUsuario

app_name = 'contacto'

urlpatterns = [
    path('contacto/', ContactoUsuario.as_view(), name='contacto'),
]