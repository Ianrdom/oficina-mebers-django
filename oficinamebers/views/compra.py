from rest_framework.viewsets import ModelViewSet

from oficinamebers.models import Compra
from oficinamebers.serializers import CompraSerializer


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
