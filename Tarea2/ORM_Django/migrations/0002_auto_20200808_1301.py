# Generated by Django 3.0.8 on 2020-08-08 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ORM_Django', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['-nombre'], 'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ['descripcion'], 'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]