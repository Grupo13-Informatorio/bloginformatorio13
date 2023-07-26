from django.forms import CheckboxInput, ChoiceField, FileInput, ModelForm, TextInput, Textarea 
from apps.articulo.models import Articulo, Categoria

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
        
        
class CategoriaForm(ModelForm):
    
    class Meta:
        model = Categoria
        exclude = ['pk']
        widgets = {
            'categoria' : TextInput(attrs={'placeholder': 'Ingrese su categoria', 'max_length' : 50}),
       
        }
