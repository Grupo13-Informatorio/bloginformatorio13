from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from .views import IndexView, contacto, sobre_nosotros,registrarse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView.as_view(), name = "inicio"),
    path('contacto/', contacto, name="contacto"),
    path('registrar/', registrarse, name="registrarse"),
    path('sobre_nosotros/', sobre_nosotros, name="sobre_nosotros"),
    path('', include('apps.articulo.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 

