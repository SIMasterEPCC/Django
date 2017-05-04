# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Temperatura(models.Model):
    temp_grados_celsius = models.CharField(max_length=20)
    temp_grados_farenheit = models.CharField(max_length=20)
    humedad = models.CharField(max_length=20)
    presion = models.CharField(max_length=20)
    velocidad_viento = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)

class Admin:
    pass