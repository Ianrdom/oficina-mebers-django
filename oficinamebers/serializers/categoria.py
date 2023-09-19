from rest_framework.serializers import ModelSerializer
from oficinamebers.models import Categoria


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"
