# Generated by Django 4.2.2 on 2023-06-15 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0004_alter_producto_mantenimientolicitado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='tipoEquipo',
            field=models.TextField(verbose_name='Tipo de Equipo'),
        ),
    ]
