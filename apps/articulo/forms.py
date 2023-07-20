from django.forms import CharField, ImageField, ModelForm, TextInput, Textarea

from apps.articulo.models import Articulo

class ArticuloCreationForm(ModelForm):

    class Meta:
        model = Articulo
        fields = ('titulo', 'resumen', 'contenido', 'categoria', 'imagen', 'is_active')