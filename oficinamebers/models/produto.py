from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=1000)
    categoria = models.ForeignKey("Categoria", on_delete=models.PROTECT)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    # como fazer imagem associar varias ao produto, ver o projeto feito do fl0 e usar manytomanyfield
    def __str__(self):
        return self.descricao
