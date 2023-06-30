from django.urls import include, path
from .views import ArticuloView

urlpatterns = [
    path('articulos/',ArticuloView.as_view(), name = 'articulos')
]