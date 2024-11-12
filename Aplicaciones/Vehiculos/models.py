from django.db import models
from django.contrib.auth.models import User

class Vehiculos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    placas = models.CharField(max_length=100, null=False, blank=False)
    tipo_vehiculo = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return f"{self.tipo_vehiculo}"
class Mantenimiento(models.Model):
    vehiculo = models.ForeignKey(Vehiculos, on_delete=models.CASCADE)
    estado = models.BooleanField(blank=False, null=False)
    descripcion = models.CharField(max_length=255, blank=False, null=False)
    fecha_mantenimiento = models.DateTimeField(auto_now_add=True)
    

from django.db import models

class Mantenimientos_km(models.Model):
    unidad = models.ForeignKey(Vehiculos, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    km_al_momento = models.IntegerField()
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Mantenimiento de {self.unidad} - {self.fecha}"