from rest_framework.viewsets import ModelViewSet

from oficinamebers.models import Cliente
from oficinamebers.serializers import ClienteSerializer


class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
