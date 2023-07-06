from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from .views import contacto, index, sobre_nosotros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name = "inicio"),
    path('contacto/', contacto, name="contacto"),
    path('sobre_nosotros/', sobre_nosotros, name="sobre_nosotros"),

    path('', include('apps.articulo.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 

