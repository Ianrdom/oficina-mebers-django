from django.contrib import admin

# Register your models here.
from oficinamebers.models import Gerente, Cliente, Vendedor

admin.site.register(Gerente)
admin.site.register(Cliente)
admin.site.register(Vendedor)
