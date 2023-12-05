from rest_framework import serializers
from oficinamebers.models import Produto, ImagensProduto
from uploader.models import Image
from uploader.serializers import ImageSerializer


class ProdutoSerializer(serializers.ModelSerializer):
    imagem_attachment_key = serializers.SlugRelatedField(
        source="imagem",
        queryset=Image.objects.all(),  # pylint: disable=no-member
        slug_field="attachment_key",
        many=True,
        required=False,
        write_only=True,
    )
    imagens = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Produto
        fields = (
            "id",
            "nome",
            "descricao",
            "categoria",
            "preco",
            "imagens",
            "quantidade",
            "imagem_attachment_key",
        )


class ImageProdutoSerializer(serializers.ModelSerializer):
    imagem = ImageSerializer(read_only=True)

    class Meta:
        model = ImagensProduto
        fields = (
            "imagem",
            "id",
            "principal",
        )


class ProdutoDetailSerializer(serializers.ModelSerializer):
    imagens = ImageProdutoSerializer(many=True, read_only=True)
    categoria = serializers.CharField(source="categoria.descricao")

    class Meta:
        model = Produto
        fields = (
            "id",
            "nome",
            "descricao",
            "categoria",
            "preco",
            "quantidade",
            "imagens",
        )
