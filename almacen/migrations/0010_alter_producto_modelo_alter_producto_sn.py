# Generated by Django 4.2.2 on 2023-06-15 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0009_alter_producto_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='modelo',
            field=models.TextField(verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='sn',
            field=models.TextField(max_length=1000, verbose_name='SN'),
        ),
    ]
