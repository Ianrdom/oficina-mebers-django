from django.db import models
from usuario.models import Usuario


class Cliente(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Clientes"
