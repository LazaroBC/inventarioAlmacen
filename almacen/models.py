from django.db import models

# Create your models here.


class Almacen(models.Model):
    idAlmacen = models.AutoField(primary_key=True)
    nombreAlmacen = models.CharField(max_length=50)
    direccionAlmacen = models.CharField(max_length=50)
    telefonoAlmacen = models.CharField(max_length=50)
    emailAlmacen = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreAlmacen


class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    foto1 = models.ImageField(
        upload_to='almacen/static/img', null=True, blank=True, verbose_name= "Imagenes")
    foto2 = models.ImageField(
        upload_to='almacen/static/img', null=True, blank=True, verbose_name= "Imagenes")
    foto3 = models.ImageField(
        upload_to='almacen/static/img', null=True, blank=True, verbose_name= "Imagenes")
    manualInstrucciones = models.FileField(
        upload_to='almacen/static/docs', null=True, blank=True, verbose_name= "Documentos")
    tipoEquipo = models.CharField(null=True, blank=True, max_length=1000)
    subtipoEquipo = models.CharField(null=True, blank=True, max_length=1000)
    numeroInventario = models.IntegerField(
        null=True, blank=True, verbose_name="Numero de Inventario")
    mantenimientoLicitado = models.BooleanField(
        null=True, blank=True, verbose_name="Mantenimiento Licitado")
    numeroMantenedor = models.IntegerField(
        null=True, blank=True, verbose_name="Numero de Mantenedor")
    marca = models.CharField(null=True, blank=True, max_length=1000, verbose_name="Marca")
    modelo = models.CharField(null=True, blank=True, max_length=1000, verbose_name="Modelo")
    anyoFabricacion = models.IntegerField(
        null=True, blank=True, verbose_name="Año de Fabricacion")
    sn = models.CharField(null=True, blank=True, max_length=1000, verbose_name="SN")
    nref = models.CharField(null=True, blank=True, max_length=1000, verbose_name="NREF")
    descripcion = models.CharField(null=True, blank=True, max_length=1000, verbose_name="Descripcion")
    comentarios = models.CharField(null=True, blank=True, max_length=1000, verbose_name="Comentarios")
    estado = models.CharField(null=True, blank=True, max_length=1000, verbose_name="Estado")
    anyoCompra = models.IntegerField(
        null=True, blank=True, verbose_name="Año de Compra")
    numExpContratacion = models.IntegerField(
        null=True, blank=True, verbose_name="Numero de Expediente de Contratacion")
    tiquetsReferenciaMantenedor = models.IntegerField(
        null=True, blank=True, verbose_name="Tiquets de Referencia del Mantenedor")
    tiquetsReferenciaMantUV = models.IntegerField(
        null=True, blank=True, verbose_name="Tiquets de Referencia del Mantenedor UV")
    tiquetsRefTiquetingFLA = models.IntegerField(
        null=True, blank=True, verbose_name="Tiquets de Referencia del Tiqueting FLA")
    otros = models.CharField(null=True, blank=True, max_length=1000, verbose_name="Otros")
    clinica = models.CharField(null=True, blank=True, max_length=1000, verbose_name="Clinica")
    ubicacion = models.CharField(null=True, blank=True, max_length=1000, verbose_name="Ubicacion")

    def __str__(self):
        return self.tipoEquipo
    
    # Borrado de imagenes y documentos
    def delete(self, using=None, keep_parents=False):
        self.foto1.storage.delete(self.foto1.name)
        self.foto2.storage.delete(self.foto2.name)
        self.foto3.storage.delete(self.foto3.name)
        self.manualInstrucciones.delete(self.manualInstrucciones.name)
        super().delete()
