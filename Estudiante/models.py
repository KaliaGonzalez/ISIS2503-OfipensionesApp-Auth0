from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50) 
    edad = models.IntegerField() 
    curso = models.CharField(max_length=50)  
    matricula = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return '{}'.format(self.nombre)

