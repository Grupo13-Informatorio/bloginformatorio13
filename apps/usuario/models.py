from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Usuario(AbstractUser):
    is_colaborador = models.BooleanField(
        verbose_name="Colaborador",
        default=False,
    )
    is_publico = models.BooleanField(
        verbose_name="Publico",
        default=True
    )