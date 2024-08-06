from rest_framework import serializers
from .models import ExAlumno

class ExAlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExAlumno
        fields = '__all__'