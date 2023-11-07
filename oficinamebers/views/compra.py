from rest_framework.viewsets import ModelViewSet

from oficinamebers.models import Compra
from oficinamebers.serializers import CompraSerializer, CriarEditarCompraSerializer


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return CriarEditarCompraSerializer
        return CompraSerializer
