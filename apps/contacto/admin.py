from django.contrib import admin
from .models import Contacto

@admin.register(Contacto)
class ContactoModels(admin.ModelAdmin):
    list_display = ('id','nombre_apellido','email','asunto','fecha')

# Register your models here.
