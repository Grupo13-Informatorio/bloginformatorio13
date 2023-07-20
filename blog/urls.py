from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from .views import IndexView, contacto, registration_success, sobre_nosotros,registrarse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView.as_view(), name = "inicio"),
    path('contacto/', contacto, name="contacto"),
    path('nosotros/', sobre_nosotros, name="nosotros"),
    path('', include('apps.articulo.urls')),
    path('', include('apps.usuario.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path("acounts/registration/success/",registration_success, name='registration_success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

