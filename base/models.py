from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from sports_bets.base.choices import RESULTS, KINDS


class Liga(models.Model):
    pais = models.CharField(max_length=100)


class Equipo(models.Model):
    nombre = models.CharField(max_length=100)


class Partido(models.Model):
    fecha = models.DateTimeField()
    equipo_local = models.ForeignKey(Equipo, on_delete=models.CASCADE, verbose_name=_('equipo_local'))
    equipo_visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, verbose_name=_('equipo_visitante'))
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE, verbose_name=_('liga'))


class Quiniela(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    puntuacion_maxima = models.IntegerField()
    descripcion = models.TextField()


class Seleccion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    quiniela = models.ForeignKey(Quiniela, on_delete=models.CASCADE)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    resultado = models.CharField(max_length=10, choices=RESULTS, default='local', verbose_name=_('resultado'))
    tipo = models.CharField(max_length=10, choices=KINDS, default='local', verbose_name=_('tipo_de_seleccion'))


class Puntuacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    quiniela = models.ForeignKey(Quiniela, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()


class Resultado(models.Model):
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    resultado_real = models.CharField(max_length=10)  # Ej. "ganar", "perder", "empate"
