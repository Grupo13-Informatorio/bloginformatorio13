from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Usuario(AbstractUser):
    is_visitante = models.BooleanField(default=True)
    is_miembro = models.BooleanField(default=False)
    is_usuario = models.BooleanField(default=False)
    foto_perfil = models.ImageField(
        default="static/default-user.png", 
        upload_to="media/usuarios",
        blank=True,
        null=True
        )
