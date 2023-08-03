from django.contrib.auth.models import Group, User, Permission
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy

import datetime

# Create your models here.


class Usuario(AbstractUser):
    is_miembro = models.BooleanField(default=False)
    foto_perfil = models.ImageField(upload_to="usuario",
        default="../static/default-user.png"
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




