from django.db import models
from datetime import datetime
from django.utils.timezone import now

class Comentario(models.Model):
    texto = models.CharField(max_length=500)
    nombre = models.CharField(max_length=60)
    color = models.CharField(max_length=500)
    fecha = models.DateTimeField(default=now)
