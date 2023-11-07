from rest_framework.serializers import ModelSerializer, CharField

from oficinamebers.models import Compra


class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = "__all__"
