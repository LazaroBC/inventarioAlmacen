from django.db import models
from django.core.validators import MaxValueValidator
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
    id = models.AutoField(primary_key=True)
    foto1 = models.ImageField(
        upload_to='almacen/static/img', null=True, blank=True, verbose_name= "Imagenes")
    foto2 = models.ImageField(
        upload_to='almacen/static/img', null=True, blank=True, verbose_name= "Imagenes")
    foto3 = models.ImageField(
        upload_to='almacen/static/img', null=True, blank=True, verbose_name= "Imagenes")
    manualInstrucciones = models.FileField(
        upload_to='almacen/static/docs', null=True, blank=True, verbose_name= "Documentos")
    tipoEquipo = models.TextField(null=False, blank=False, verbose_name="Tipo de Equipo")
    subtipoEquipo = models.TextField(null=True, blank=True, verbose_name="Subtipo de Equipo")
    numeroInventario = models.TextField(null=False, blank=False, verbose_name="Numero de Inventario")
    mantenimientoLicitado = models.BooleanField(null=False, blank=False, verbose_name="Mantenimiento Licitado")
    numeroMantenedor = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(9999)], verbose_name="Numero de Mantenedor")
    marca = models.TextField(null=False, blank=False, verbose_name="Marca")
    modelo = models.TextField(null=False, blank=False, verbose_name="Modelo")
    anyoFabricacion = models.IntegerField(null=True, blank=True,  validators=[MaxValueValidator(9999)], verbose_name="Año de Fabricacion")
    sn = models.TextField(null=False, blank=False, verbose_name="SN")
    nref = models.TextField(null=True, blank=True, verbose_name="NREF")
    descripcion = models.TextField(null=True, blank=True, verbose_name="Descripcion")
    comentarios = models.TextField(null=True, blank=True, verbose_name="Comentarios")
    estado = models.TextField(null=True, blank=True, verbose_name="Estado")
    anyoCompra = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(9999)],verbose_name="Año de Compra")
    numExpContratacion = models.TextField(null=True, blank=True, verbose_name="Numero de Expediente de Contratacion")
    tiquetsReferenciaMantenedor = models.TextField(null=True, blank=True, verbose_name="Tiquets de Referencia del Mantenedor")
    tiquetsReferenciaMantUV = models.TextField(null=True, blank=True, verbose_name="Tiquets de Referencia del Mantenedor UV")
    tiquetsRefTiquetingFLA = models.TextField(null=True, blank=True, verbose_name="Tiquets de Referencia del Tiqueting FLA")
    otros = models.TextField(null=True, blank=True, verbose_name="Otros")
    clinica = models.TextField(null=True, blank=True, verbose_name="Clinica")
    ubicacion = models.TextField(null=True, blank=True, verbose_name="Ubicacion")

    def __str__(self):
        return self.tipoEquipo
    
    # Borrado de imagenes y documentos
    def delete(self, using=None, keep_parents=False):
        self.foto1.storage.delete(self.foto1.name)
        self.foto2.storage.delete(self.foto2.name)
        self.foto3.storage.delete(self.foto3.name)
        self.manualInstrucciones.delete(self.manualInstrucciones.name)
        super().delete()
