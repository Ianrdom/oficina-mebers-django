from django.db import models


class Compra(models.Model):
    descricao = models.CharField(max_length=1000)
    produto = models.ForeignKey("Produto", on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao
