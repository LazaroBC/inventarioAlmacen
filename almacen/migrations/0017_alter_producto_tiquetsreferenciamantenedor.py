# Generated by Django 4.2.2 on 2023-06-15 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0016_alter_producto_numexpcontratacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='tiquetsReferenciaMantenedor',
            field=models.TextField(blank=True, null=True, verbose_name='Tiquets de Referencia del Mantenedor'),
        ),
    ]
