from django.forms import CharField, ImageField, ModelForm, TextInput, Textarea

from apps.articulo.models import Articulo

class ArticuloCreationForm(ModelForm):

    class Meta:
        model = Articulo
        exclude = ['creado_por', 'fecha', 'modificado']