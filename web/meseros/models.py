from django.db import models

# Create your models here.

class Restaurante(models.Model):
    nombre = models.CharField(max_length=80)
    tipo = models.CharField(max_length=80)

class Sucursal(models.Model):
    noExterior = models.IntegerField()
    noInterior = models.IntegerField()
    colonia = models.CharField(max_length=120)
    cp = models.IntegerField()
    ciudad = models.CharField(max_length=50, null=True, blank=True)
    estado = models.CharField(max_length=50, null=True, blank=True)
    noEmpleados = models.SmallIntegerField()
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)

class Mesero(models.Model):
    nombre = models.CharField(max_length=80)
    fechaNacimiento = models.DateField()

class Evento(models.Model):
    nombre = models.CharField(max_length=120)
    fecha = models.DateField()

class MeseroEvento(models.Model):
    mesero = models.ForeignKey(Mesero, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    uniforme = models.BooleanField()
    horaInicio = models.TimeField()
    horaFin = models.TimeField()

class MeseroSucursal(models.Model):
    mesero = models.ForeignKey(Mesero, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    turno = models.CharField(max_length=50, null=True, blank=True)

