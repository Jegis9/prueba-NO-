# Generated by Django 5.1 on 2024-10-17 17:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('institucion', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Habilidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=100)),
                ('sobre_mi', models.CharField(max_length=100)),
                ('tipo_sangre', models.CharField(max_length=10)),
                ('contacto_telefono_emergencia', models.CharField(blank=True, max_length=15, null=True)),
                ('contacto_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('estado', models.CharField(max_length=100)),
                ('certificaciones', models.ManyToManyField(to='Personal.certificacion')),
                ('habilidades', models.ManyToManyField(to='Personal.habilidad')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('cargo', models.CharField(max_length=100)),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiencias', to='Personal.personal')),
            ],
        ),
        migrations.CreateModel(
            name='Educacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('institucion', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educaciones', to='Personal.personal')),
            ],
        ),
    ]