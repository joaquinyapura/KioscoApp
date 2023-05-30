from django.contrib import admin
from .models import Proveedor, Producto, Usuario, Cliente

# Register your models here.


admin.site.register(Producto)
admin.site.register(Usuario)


class Clientes(admin.ModelAdmin):
    list_display = ('nombre', 'importe')


admin.site.register(Cliente, Clientes)


class Proveedores(admin.ModelAdmin):
    list_display = ('nombre_prov', 'telefono')


admin.site.register(Proveedor, Proveedores)
