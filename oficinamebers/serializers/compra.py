from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from oficinamebers.models import Compra, ItensCompra


class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    def get_total(self, instance):
        return instance.quantidade * instance.livro.preco

    class Meta:
        model = ItensCompra
        fields = ["produto", "quantidade"]
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

    def create(self, validated_data):
        itens_data = validated_data.pop("itens")
        compra = Compra.objects.create(**validated_data)
        for item_data in itens_data:
            ItensCompra.objects.create(compra=compra, **item_data)
        compra.save()
        return compra


class CompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True)
    status = CharField(source="get_status_display", read_only=True)
    itens = ItensCompraSerializer(many=True, read_only=True)

    @property
    def total(self):
        return sum(item.livro.preco * item.quantidade for item in self.itens.all())

    def update(self, instance, validated_data):
        itens = validated_data.pop("itens")
        if itens:
            instance.itens.all().delete()
            for item in itens:
                ItensCompra.objects.create(compra=instance, **item)
        instance.save()
        return instance

    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "itens")
