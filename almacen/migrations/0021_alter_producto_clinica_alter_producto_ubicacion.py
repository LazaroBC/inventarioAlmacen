# Generated by Django 4.2.2 on 2023-06-15 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0020_alter_producto_otros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='clinica',
            field=models.TextField(blank=True, null=True, verbose_name='Clinica'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='ubicacion',
            field=models.TextField(blank=True, null=True, verbose_name='Ubicacion'),
        ),
    ]
