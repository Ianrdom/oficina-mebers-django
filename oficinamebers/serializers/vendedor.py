from rest_framework.serializers import ModelSerializer
from oficinamebers.models import Vendedor


class VendedorSerializer(ModelSerializer):
    class Meta:
        model = Vendedor
        fields = "__all__"
