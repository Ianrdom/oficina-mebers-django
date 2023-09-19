from rest_framework import serializers
from oficinamebers.models import Produto
from uploader.models import Image
from uploader.serializers import ImageSerializer


class ProdutoSerializer(serializers.ModelSerializer):
    cover_attachment_key = serializers.SlugRelatedField(
        source="cover",
        queryset=Image.objects.all(),  # pylint: disable=no-member
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    cover = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Produto
        fields = (
            "id",
            "nome",
            "descricao",
            "categoria",
            "preco",
            "cover",
            "cover_attachment_key",
        )


class ProdutoDetailSerializer(serializers.ModelSerializer):
    cover = ImageSerializer(required=False)
    genre = serializers.CharField(source="genre.name")

    class Meta:
        model = Produto
        fields = ("id", "title", "year", "rating", "genre", "cover")
