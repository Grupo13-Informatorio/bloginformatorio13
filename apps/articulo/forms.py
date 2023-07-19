from django.forms import CharField, ImageField, ModelForm, TextInput, Textarea

from apps.articulo.models import Articulo

class ArticuloCreationForm(ModelForm):
    titulo = CharField(
        label='Titulo', 
        max_length=35,
        min_length=3,
        widget=TextInput(
            attrs={'placeholder': 'Igrese el titulo del articulo.'}
            )
        )
    resumen = CharField(
        label='Reseña', 
        max_length=250,
        min_length=10,
        widget=TextInput(
            attrs={'placeholder': 'Igrese un breve resumen. Maximo 250 caracteres.'}
            )
        )
    contenido = Textarea(
        )
    
    class Meta:
        model = Articulo
        fields = ('titulo', 'resumen', 'contenido', 'categoria', 'imagen', 'is_active')