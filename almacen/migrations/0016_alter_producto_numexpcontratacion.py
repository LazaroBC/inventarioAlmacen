# Generated by Django 4.2.2 on 2023-06-15 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0015_alter_producto_anyocompra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='numExpContratacion',
            field=models.TextField(blank=True, null=True, verbose_name='Numero de Expediente de Contratacion'),
        ),
    ]
