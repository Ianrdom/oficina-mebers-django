from rest_framework import viewsets

from oficinamebers.models import Produto
from oficinamebers.serializers import ProdutoSerializer
from oficinamebers.serializers import ProdutoDetailSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()  # pylint: disable = E1101
    serializer_class = ProdutoSerializer

    def get_serializer_class(self):
        if self.action in ["retrieve", "list"]:
            return ProdutoDetailSerializer
        return super().get_serializer_class()
