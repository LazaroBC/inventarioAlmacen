# Generated by Django 4.2.2 on 2023-06-15 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0003_rename_idproducto_producto_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='mantenimientoLicitado',
            field=models.BooleanField(verbose_name='Mantenimiento Licitado'),
        ),
    ]