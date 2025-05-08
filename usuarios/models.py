from django.db import models
from django.contrib.auth.hashers import make_password


# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    id_usuario = models.IntegerField(unique=True)  # ID numérico único
    contraseña = models.CharField(max_length=128)  # Almacena la contraseña encriptada

    def save(self, *args, **kwargs):
        if not self.pk or 'contraseña' in kwargs:  # Encripta solo si es nuevo o cambia
            self.contraseña = make_password(self.contraseña)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre