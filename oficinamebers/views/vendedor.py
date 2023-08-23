from rest_framework.viewsets import ModelViewSet

from oficinamebers.models import Vendedor
from oficinamebers.serializers import VendedorSerializer


class VendedorViewSet(ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer
