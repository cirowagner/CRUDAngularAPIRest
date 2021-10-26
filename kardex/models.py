from django.db import models

# Create your models here.
class Marca(models.Model):

    descripcion=models.CharField(max_length=40)
    logo=models.ImageField(upload_to='marca', null=True, blank=True)

    class Meta:
        verbose_name = ("Marca")
        verbose_name_plural = ("Marcas")

    def _str_(self):
        return self.descripcion

class Grupo(models.Model):

    descripcion=models.CharField(max_length=30)
    grupo_id=models.ForeignKey("Grupo", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Grupo")
        verbose_name_plural = ("Grupos")

    def _str_(self):
        return self.descripcion


TIPO_MEDIDA=[
    ('BJ','BALDE'),
    ('BG','BOLSA'),
    ('BX','CAJA'),
    ('KGM','KILOGRAMO'),
    ('LTR','LITRO'),
    ('NIU','UNIDAD'),
]
class Producto(models.Model):

    marca=models.ForeignKey("Marca", on_delete=models.CASCADE)
    medida=models.CharField(max_length=20,choices=TIPO_MEDIDA)
    grupo=models.ForeignKey("Grupo", on_delete=models.CASCADE)
    codigo=models.CharField(max_length=20)
    nombre=models.CharField(max_length=15)
    descripcion=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='producto', null=True, blank=True)
    maximo=models.IntegerField()
    minimo=models.IntegerField()
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = ("Producto")
        verbose_name_plural = ("Productos")

    def _str_(self):
        return self.nombre

class Proveedor(models.Model):

    razonsocial=models.CharField(max_length=30)
    ruc=models.CharField(max_length=15)
    direccion=models.CharField(max_length=40)
    ciudad=models.CharField(max_length=20)
    celular1=models.CharField(max_length=15)
    celular2=models.CharField(max_length=15)
    telefono1=models.CharField(max_length=15)
    telefono2=models.CharField(max_length=15)
    contacto=models.CharField(max_length=45)
    email=models.EmailField(max_length=50)
    paginaweb=models.CharField(max_length=30)
    banco=models.CharField(max_length=30)
    cuenta=models.CharField(max_length=40)

    class Meta:
        verbose_name = ("Proveedor")
        verbose_name_plural = ("Proveedors")

    def _str_(self):
        return self.razonsocial

TIPO_OPERACION=[
    ('VENTA','VENTA NACIONAL'),
    ('COMPRA','COMPRA NACIONAL'),
    ('DEVOLUCION','DEVOLUCION RECIBIDA'),
    ('OTROS','OTROS'),
]
TIPO_COMPROBANTE=[
    ('FACTURA','FACTURA'),
    ('BOLETA','BOLETA DE VENTA'),
    ('GUIA','GUIA DE REMISION'),
    ('OTROS','OTROS'),
]

class Kardex(models.Model):

    producto=models.ForeignKey("Producto", on_delete=models.CASCADE)
    toperacion=models.CharField(max_length=50, choices=TIPO_OPERACION)
    tcomprobante=models.CharField(max_length=20, choices=TIPO_COMPROBANTE)
    proveedor=models.ForeignKey("Proveedor", on_delete=models.CASCADE)
    fecha=models.DateField()
    serie=models.CharField(max_length=8)
    numero=models.CharField(max_length=10)
    ecantidad=models.IntegerField()
    ecostou=models.FloatField()
    ecostot=models.FloatField()
    xcantidad=models.IntegerField()
    xcostou=models.FloatField()
    xcostot=models.FloatField()
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = ("Kardex")
        verbose_name_plural = ("Kardexs")

    def _str_(self):
        return self.fecha