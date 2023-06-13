from django.db import models


class Gerente(models.Model):
    nome = models.CharField(default="GerenteAutomatico", max_length=255)
    email = models.EmailField(default="email@gmail.com", null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Gerentes"
