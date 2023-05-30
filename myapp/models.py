from django.db import models

# Create your models here.


class Proveedor(models.Model):
    nombre_prov = models.CharField(max_length=50)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre_prov


class Producto(models.Model):
    nombre_prod = models.CharField(max_length=50)
    cant_caja = models.CharField(max_length=50)
    precio_caja = models.IntegerField()
    link_foto = models.URLField()
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_prod


class Usuario(models.Model):
    usuario = models.CharField(max_length=50)
    contra = models.CharField(max_length=50)

    def __str__(self):
        return self.usuario


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    importe = models.IntegerField()

    def __str__(self):
        return self.nombre
