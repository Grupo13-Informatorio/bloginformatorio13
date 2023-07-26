from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

import datetime
# Create your models here.


class Usuario(AbstractUser):
    is_miembro = models.BooleanField(default=False)
    is_usuario = models.BooleanField(default=True)
    foto_perfil = models.ImageField(
        default="../static/default-user.png", 
        upload_to="usuarios",
        )
    fecha_nacimiento = models.DateField(
        null=True,
        blank=True
    )
    
    def get_edad(self):
        return int((datetime.date.today() - self.fecha_nacimiento).days / 365.25)
    
    def __str__(self):
        return self.username
    
    def get_link_verperfil(self):
        return reverse ('usuario:ver', args=[ self.pk ])
    
