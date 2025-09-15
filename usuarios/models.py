from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20, blank=True)
    tipo_usuario = models.CharField(
        max_length=20,
        choices=[
            ("administrador", "Administrador"),
            ("contador", "Contador"),
            ("cliente", "Cliente"),
        ],
        default="cliente",
    )

    def __str__(self):
        return self.user.username
