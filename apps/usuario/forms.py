from typing import Any, Dict
from django.forms import CharField, DateField, ModelForm, PasswordInput

from apps.usuario.models import Usuario


class UserCreationForm(ModelForm):
    password = CharField(
        label='Contraseña', 
        widget=PasswordInput(
            attrs={'placeholder': 'Contraseña'}
            ), 
        required=True)
    password2 = CharField(
        label='Reingrese Contraseña', 
        widget=PasswordInput(
            attrs={'placeholder': 'Reingrese su contraseña'}
            ), 
        required=True)
    fecha_nacimiento = DateField(
        label="Ingrese fecha de nacimiento"
    )
    
    def clean(self):
        cleaned_form = super().clean() 
        password = cleaned_form.get('password')
        password2 = cleaned_form.get('password2')
        if password != password2:
            self.add_error("password2", "Las contraseñas no coinciden")
        return cleaned_form
    
    class Meta:
        model = Usuario
        fields = ('first_name','last_name','email','fecha_nacimiento', 'username', 'password', 'foto_perfil')

