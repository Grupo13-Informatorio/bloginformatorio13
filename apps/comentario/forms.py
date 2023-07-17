from django.forms import CharField, ModelForm, TextInput

from apps.comentario.models import Comentario


class ComentarioCreationForm(ModelForm):
    contenido = CharField(
        label='Ingrese aqui su comentario', 
        max_length=250,
        min_length=30,
        widget=TextInput(
            attrs={'placeholder': 'Igrese su comentario. Maximo 250 caracteres.'}
            )
        )
    
    class Meta:
        model = Comentario
        fields = ('contenido',)