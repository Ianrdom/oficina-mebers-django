from rest_framework.viewsets import ModelViewSet

from oficinamebers.models import Gerente
from oficinamebers.serializers import GerenteSerializer


class GerenteViewSet(ModelViewSet):
    queryset = Gerente.objects.all()
    serializer_class = GerenteSerializer
