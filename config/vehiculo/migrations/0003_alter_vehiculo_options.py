# Generated by Django 4.0.5 on 2024-11-16 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0002_alter_vehiculo_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'permissions': [('visualizar_vehiculo', 'Puede visualizar el catálogo de vehículos')]},
        ),
    ]