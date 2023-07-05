"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
##from .views import index
from .views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    ##Esta linea de abajo tendría que reemplazarse por la de HOME ya que es la que aparece al inicio
    path('', IndexView.as_view(), name='index'),
    ##En esta linea de abajo estoy usando el articulo.html de la carpeta templates que lo llamo desde la views.py de articulo, pero antes se va a buscarlo a la urls.py de articulo
    path('', include('apps.articulo.urls')),
]
