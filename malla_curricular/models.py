from django.db import models

# Create your models here.
class Facultad(models.Model):
    nombre = models.CharField(max_length=50)
    siglas = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.nombre} - ({self.siglas})'

class Carrera(models.Model):
    nombre = models.CharField(max_length=50)
    siglas = models.CharField(max_length=10)
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nombre} - ({self.siglas})'

class Ciclo(models.Model):
    nombre = models.PositiveIntegerField()
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nombre} - {self.carrera}'
class Asignatura(models.Model):
    nombre = models.CharField(max_length=50)
    siglas = models.CharField(max_length=10)
    ape = models.PositiveIntegerField()
    acd = models.PositiveIntegerField()
    pp = models.PositiveIntegerField()
    aa = models.PositiveIntegerField()
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nombre} - ({self.siglas})'