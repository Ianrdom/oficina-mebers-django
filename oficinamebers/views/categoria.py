from rest_framework.viewsets import ModelViewSet

from oficinamebers.models import Produto
from oficinamebers.serializers import ProdutoSerializer


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
