from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from .views import IndexView, registration_success, sobre_nosotros

urlpatterns = [
    path('jpqifepfnapkjdfnapdjk/', admin.site.urls),
    path('',IndexView.as_view(), name = "inicio"),
    path('nosotros/', sobre_nosotros, name="nosotros"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("acounts/registration/success/",registration_success, name='registration_success'),
    path('', include('apps.articulo.urls')),
    path('', include('apps.usuario.urls')),
    path('', include('apps.comentario.urls')),
    path('', include('apps.contacto.urls')),
    path("", include("allauth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

