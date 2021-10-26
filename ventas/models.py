from django.db import models
from kardex.models import Producto

# Create your models here.
class Cliente(models.Model):

    dni=models.CharField(max_length=8)
    nombre=models.CharField(max_length=50)
    ruc=models.CharField(max_length=10)
    razon=models.CharField(max_length=50)
    direccion=models.CharField(max_length=70)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)


    class Meta:
        verbose_name = ("Cliente")
        verbose_name_plural = ("Clientes")

    def _str_(self):
        return self.nombre

TIPO_COMPROBANTE=[
    ('FACTURA','FACTURA'),
    ('BOLETA','BOLETA DE VENTA'),
    ('GUIA','GUIA DE REMISION'),
    ('OTROS','OTROS'),
]
class Comprobante(models.Model):

    cliente=models.ForeignKey("Cliente", on_delete=models.CASCADE)
    tcomprobante=models.CharField(max_length=20, choices=TIPO_COMPROBANTE)
    numfactura=models.CharField(max_length=10)
    numboleta=models.CharField(max_length=10)
    fecha=models.DateField()
    igv=models.DecimalField(max_digits=10, decimal_places=2)
    total=models.DecimalField(max_digits=10, decimal_places=2)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)


    class Meta:
        verbose_name = ("Comprobante")
        verbose_name_plural = ("Comprobantes")

    def _str_(self):
        return self.tcomprobante


class Detalle(models.Model):

    comprobante=models.ForeignKey("Comprobante", on_delete=models.CASCADE)
    cantidad=models.IntegerField()
    producto=models.ForeignKey("kardex.Producto", on_delete=models.CASCADE)
    importe=models.FloatField()
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)

    class Meta:
        verbose_name = ("Detalle")
        verbose_name_plural = ("Detalles")

    def _str_(self):
        return self.cantidad
