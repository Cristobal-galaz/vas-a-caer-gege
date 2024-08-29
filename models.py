# models.py
from django.db import models
from django.contrib.auth.models import User


class IA(models.Model):
    #id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)









class Favorita(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    ia = models.ForeignKey('IA', on_delete=models.CASCADE)
    
def __str__(self):
    return f"{self.usuario.username} - {self.ia.nombre}"