# Generated by Django 4.2.2 on 2023-06-15 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0008_alter_producto_anyofabricacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='marca',
            field=models.TextField(verbose_name='Marca'),
        ),
    ]
