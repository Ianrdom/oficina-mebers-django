from django.contrib import admin

# Register your models here.
from oficinamebers.models import (
    Gerente,
    Cliente,
    Vendedor,
    Categoria,
    Produto,
    ImagensProduto,
)

admin.site.register(Gerente)
admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(ImagensProduto)
