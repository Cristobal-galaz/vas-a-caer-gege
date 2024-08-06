# models.py
from django.db import models

class ExAlumno(models.Model):
    nombres = models.CharField(max_length=100)  # Campo obligatorio
    apellidos = models.CharField(max_length=100, blank=True, null=True)
    profesion = models.CharField(max_length=100, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    tipo_trabajo = models.CharField(max_length=100, blank=True, null=True)
    facebook_profile = models.URLField(blank=True, null=True)
    linkedin_profile = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
