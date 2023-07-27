from django.contrib.auth.models import Group, User, Permission
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy

import datetime

# Create your models here.


class Usuario(AbstractUser):
    is_miembro = models.BooleanField(default=False)
    foto_perfil = models.ImageField(
        default="../static/default-user.png", 
        upload_to="usuarios",
        )
    fecha_nacimiento = models.DateField(
        null=True,
        blank=True
    )
    
   
    def get_link_verperfil(self):
        return reverse_lazy('usuario:perfil', args=[ self.pk ])
    
    def get_edad(self):
        return int((datetime.date.today() - self.fecha_nacimiento).days / 365.25)
    
    def __str__(self):
        return self.username
    
    def save(self, force_insert, force_update, using, update_fields):
        if self.is_miembro:
            pass            
        else:
            pass
        return super().save(force_insert, force_update, using, update_fields)
    
    
    

    
