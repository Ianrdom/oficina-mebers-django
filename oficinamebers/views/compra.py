from rest_framework.viewsets import ModelViewSet

from oficinamebers.models import Compra
from oficinamebers.serializers import CompraSerializer, CriarEditarCompraSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]

    filterset_fields = ["usuario", "status", "data"]
    ordering_fields = ["usuario", "status", "data"]

    def get_queryset(self):
        usuario = self.request.user
        if usuario.is_superuser:
            return Compra.objects.all()
        if usuario.groups.filter(name="Administradores"):
            return Compra.objects.all()
        return Compra.objects.filter(usuario=usuario)

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return CriarEditarCompraSerializer
        return CompraSerializer
