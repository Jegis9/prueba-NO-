# Generated by Django 5.1 on 2024-11-07 17:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Emergencias', '0001_initial'),
        ('Vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='unidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicios', to='Vehiculos.vehiculos'),
        ),
    ]
