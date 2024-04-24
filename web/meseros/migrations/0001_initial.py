# Generated by Django 4.2.11 on 2024-04-23 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Mesero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('fechaNacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('tipo', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noExterior', models.IntegerField()),
                ('noInterior', models.IntegerField()),
                ('colonia', models.CharField(max_length=120)),
                ('cp', models.IntegerField()),
                ('ciudad', models.CharField(blank=True, max_length=50, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('noEmpleados', models.SmallIntegerField()),
                ('restaurante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meseros.restaurante')),
            ],
        ),
        migrations.CreateModel(
            name='MeseroSucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turno', models.CharField(blank=True, max_length=50, null=True)),
                ('mesero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meseros.mesero')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meseros.sucursal')),
            ],
        ),
        migrations.CreateModel(
            name='MeseroEvento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniforme', models.BooleanField()),
                ('horaInicio', models.TimeField()),
                ('horaFin', models.TimeField()),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meseros.evento')),
                ('mesero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meseros.mesero')),
            ],
        ),
    ]