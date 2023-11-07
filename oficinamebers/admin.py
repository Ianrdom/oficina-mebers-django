from django.contrib import admin

# Register your models here.
from oficinamebers.models import Categoria, Produto, ImagensProduto, Compra, ItensCompra


class ItensCompraInline(admin.TabularInline):
    model = ItensCompra


admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(ImagensProduto)


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = [ItensCompraInline]
