from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Usuario(AbstractUser):
    is_miembro = models.BooleanField(default=False)
    is_usuario = models.BooleanField(default=True)
    foto_perfil = models.ImageField(
        default="../static/default-user.png", 
        upload_to="usuarios/",
        blank=True,
        null=True
        )
    fecha_nacimiento = models.DateField(
        null=True,
        blank=True
    )
    
    @property
    def edad(self):
        import datetime
        return int((datetime.date.today() - self.birthday).days / 365.25  )
    
    def __str__(self):
        return self.username