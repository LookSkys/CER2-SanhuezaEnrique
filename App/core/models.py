from django.db import models
from datetime import datetime


class residencia(models.Model):
    num_res = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50)
    fono = models.CharField(max_length=20)
    mail = models.EmailField(max_length=50)

    def nombre_completo(self):
        return "{} {}".format(self.nombre, self.primer_apellido)

    class Meta:
        verbose_name = 'Residencia'
        verbose_name_plural = 'Residencias'
        ordering = ['num_res']

    def __str__(self):
        return self.num_res


class correspondencia(models.Model):
    num_res = models.ForeignKey(
        residencia, null=False, blank=False, on_delete=models.RESTRICT)
    fecha_recepcion = models.DateField(default=datetime.today)
    remitente = models.CharField(max_length=50, null=False, blank=False)
    destinatario = models.CharField(max_length=50, null=False, blank=False)
    estados = (('E', 'Entregado'), ('W', 'En espera'), ('N', 'No entregado'))
    estado = models.CharField(max_length=1, choices=estados, default='W')
    conserje = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'Correspondencia'
        verbose_name_plural = 'Correspondencias'
        ordering = ['fecha_recepcion']

    def __str__(self):
        return self.destinatario
