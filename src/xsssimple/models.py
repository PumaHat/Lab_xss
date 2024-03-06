from django.db import models
from datetime import datetime

class ComentarioSimple(models.Model):
    texto = models.CharField(max_length=500)
    nombre = models.CharField(max_length=60)
    color = models.CharField(max_length=500)
    fecha = models.DateTimeField(default=datetime.now())
