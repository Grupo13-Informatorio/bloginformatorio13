from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Contacto(models.Model):
    nombre_apellido = models.CharField(max_length=120)
    email = models.EmailField()
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)
    
    def get_absolute_url(self): # new
        return reverse('inicio')

    def __str__(self) -> str:
        return self.nombre_apellido