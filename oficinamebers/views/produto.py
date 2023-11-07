from rest_framework import viewsets

from oficinamebers.models import Produto
from oficinamebers.serializers import ProdutoSerializer
from oficinamebers.serializers import ProdutoDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]

    filterset_fields = ["categoria__descricao", "categoria"]
    search_fields = ["nome"]
    ordering_fields = ["nome", "preco"]
    ordering = ["nome"]

    def get_serializer_class(self):
        if self.action in ["retrieve", "list"]:
            return ProdutoDetailSerializer
        return super().get_serializer_class()
