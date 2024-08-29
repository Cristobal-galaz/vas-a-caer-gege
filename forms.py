from django import forms
from .models import IA

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=100)
    email = forms.EmailField(label='Correo electrónico')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput())




class IAForm(forms.ModelForm):
    class Meta:
        model = IA
        fields = ['id','nombre', 'categoria', 'url','descripcion']