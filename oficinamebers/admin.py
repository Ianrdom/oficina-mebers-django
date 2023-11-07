from django.contrib import admin

# Register your models here.
from oficinamebers.models import (
    Categoria,
    Produto,
    ImagensProduto,
)


admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(ImagensProduto)
