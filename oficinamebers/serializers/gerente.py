from rest_framework.serializers import ModelSerializer
from oficinamebers.models import Gerente


class GerenteSerializer(ModelSerializer):
    class Meta:
        model = Gerente
        fields = "__all__"
