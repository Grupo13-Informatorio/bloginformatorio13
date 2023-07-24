from django.forms import CheckboxInput, FileInput, ModelForm, TextInput, Textarea 
from apps.articulo.models import Articulo

class ArticuloCreationForm(ModelForm):

    class Meta:
        model = Articulo
        widgets = {
            'titulo' : TextInput(attrs={'placeholder': 'Ingrese su titulo'}),
            'resumen' : TextInput(attrs={'placeholder': 'Ingrese aqui su resumen'}),
            'contenido' : Textarea(attrs={'rows': 6, 'placeholder': 'Ingrese aqui el articulo'}),
            'imagen': FileInput(),
        }
        exclude = ['creado_por', 'fecha', 'modificado', 'is_active']