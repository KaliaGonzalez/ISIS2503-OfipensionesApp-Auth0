from django.db import models


class Balance(models.Model):
   
    precio = models.FloatField(null=True, blank=True, default=None)
    numRegistros = models.CharField(max_length=50)
    clasificacion = models.CharField(max_length=50) 
    mes = models.CharField(max_length=50) 
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % ( self.mes)