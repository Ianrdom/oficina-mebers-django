from django.db import models
from uploader.models import Image


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=1000)
    categoria = models.ForeignKey("Categoria", on_delete=models.PROTECT)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ManyToManyField(Image)

    def __str__(self):
        return self.descricao
