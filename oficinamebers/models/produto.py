from django.db import models
from uploader.models import Image


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=1000)
    categoria = models.ForeignKey("Categoria", on_delete=models.PROTECT)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(default=0)

    def __str__(self):
        return self.descricao


class ImagensProduto(models.Model):
    produto = models.ForeignKey(
        Produto, on_delete=models.PROTECT, related_name="imagens"
    )
    imagem = models.ForeignKey(Image, on_delete=models.PROTECT)
    principal = models.BooleanField(default=False)

    def __str__(self):
        return self.produto.nome + " - " + str(self.imagem.attachment_key)
