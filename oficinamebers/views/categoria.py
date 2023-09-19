from rest_framework.viewsets import ModelViewSet

from oficinamebers.models import Categoria
from oficinamebers.serializers import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
