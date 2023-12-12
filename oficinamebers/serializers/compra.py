from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from oficinamebers.models import Compra, ItensCompra
from rest_framework import serializers


class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    def get_total(self, instance):
        return instance.quantidade * instance.produto.preco

    class Meta:
        model = ItensCompra
        fields = ["produto", "quantidade", "total"]
        depth = 2


class CriarEditarItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ("produto", "quantidade")


class CriarEditarCompraSerializer(ModelSerializer):
    itens = CriarEditarItensCompraSerializer(many=True)  # Aqui mudou

    class Meta:
        model = Compra
        fields = ("usuario", "itens")

    # def validate(self, data):
    #     if data["quantidade"] > data["produto"].quantidade:
    #         raise serializers.ValidationError(
    #             {"quantidade": "Quantidade solicitada não disponível em estoque."}
    #         )
    #     return data

    def create(self, validated_data):
        itens = validated_data.pop("itens")
        compra = Compra.objects.create(**validated_data)
        for item in itens:
            item["preco_item"] = item["produto"].preco
            ItensCompra.objects.create(compra=compra, **item)
        compra.save()
        return compra


class CompraSerializer(ModelSerializer):
    usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())
    data = serializers.DateTimeField(read_only=True)
    itens = ItensCompraSerializer(many=True)

    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "data", "total", "itens")

    def update(self, instance, validated_data):
        itens = validated_data.pop("itens")
        if itens:
            instance.itens.all().delete()
            for item in itens:
                ItensCompra.objects.create(compra=instance, **item)
        instance.save()
        return instance
