from django import forms
from django.core import validators
from .models import Contacto

class ContactoForm(forms.ModelForm):
    email = forms.EmailField(validators=[validators.EmailValidator(message='Ingrese un email válido.')])
    
    class Meta:
        model= Contacto
        fields = ['nombre_apellido', 'email', 'asunto', 'mensaje']

        