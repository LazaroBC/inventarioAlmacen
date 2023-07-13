from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, FileExtensionValidator, ValidationError
import os

# Create your models here.


class Almacen(models.Model):
    idAlmacen = models.AutoField(primary_key=True)
    nombreAlmacen = models.CharField(max_length=50)
    direccionAlmacen = models.CharField(max_length=50)
    telefonoAlmacen = models.CharField(max_length=50)
    emailAlmacen = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreAlmacen

def validate_pdf_or_zip(value):
    valid_extensions = ['.pdf', '.zip']
    ext = os.path.splitext(value.name)[1]
    if ext.lower() not in valid_extensions:
        raise ValidationError("Solo se permiten archivos PDF o ZIP.")

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    foto1 = models.ImageField(
        upload_to='img/', null=True, blank=True, verbose_name= "Imagenes")
    foto2 = models.ImageField(
        upload_to='img/', null=True, blank=True, verbose_name= "Imagenes")
    foto3 = models.ImageField(
        upload_to='img/', null=True, blank=True, verbose_name= "Imagenes")
    manualInstrucciones = models.FileField(
        upload_to='docs', null=True, blank=True, validators=[FileExtensionValidator(['pdf', 'zip']), validate_pdf_or_zip], verbose_name= "Documentos")
    tipoEquipo = models.TextField(null=False, blank=False, verbose_name="Tipo de Equipo")
    subtipoEquipo = models.TextField(null=True, blank=True, verbose_name="Subtipo de Equipo")
    numeroInventario = models.TextField(null=False, blank=False, verbose_name="Numero de Inventario")
    mantenimientoLicitado = models.BooleanField(null=False, blank=False, verbose_name="Mantenimiento Licitado")
    numeroMantenedor = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(9999, message="El valor no es correcto")], verbose_name="Numero de Mantenedor")
    marca = models.TextField(null=False, blank=False, verbose_name="Marca")
    modelo = models.TextField(null=False, blank=False, verbose_name="Modelo")
    anyoFabricacion = models.IntegerField(null=True, blank=True, validators=[
        MinValueValidator(1900, message='El año de fabricación debe ser entre 1900 y 2100.'),
        MaxValueValidator(2100, message='El año de fabricación debe ser entre 1900 y 2100.')
    ],
        verbose_name="Año de Fabricacion")
    sn = models.TextField(null=False, blank=False, verbose_name="SN")
    nref = models.TextField(null=True, blank=True, verbose_name="NREF")
    descripcion = models.TextField(null=True, blank=True, verbose_name="Descripcion")
    comentarios = models.TextField(null=True, blank=True, verbose_name="Comentarios")
    estado = models.TextField(null=True, blank=True, verbose_name="Estado")
    anyoCompra = models.IntegerField(null=True, blank=True, validators=[
        MinValueValidator(1900, message='El año de compra debe ser entre 1900 y 2100.'),
        MaxValueValidator(2100, message='El año de compra debe ser entre 1900 y 2100.')
    ],
    verbose_name="Año de Compra")
    numExpContratacion = models.TextField(null=True, blank=True, verbose_name="Numero de Expediente de Contratacion")
    tiquetsReferenciaMantenedor = models.TextField(null=True, blank=True, verbose_name="Tiquets de Referencia del Mantenedor")
    tiquetsReferenciaMantUV = models.TextField(null=True, blank=True, verbose_name="Tiquets de Referencia del Mantenedor UV")
    tiquetsRefTiquetingFLA = models.TextField(null=True, blank=True, verbose_name="Tiquets de Referencia del Tiqueting FLA")
    otros = models.TextField(null=True, blank=True, verbose_name="Otros")
    clinica = models.TextField(null=True, blank=True, verbose_name="Clinica")
    departamento = models.TextField(null=True, blank=True, verbose_name="Departamento")
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
