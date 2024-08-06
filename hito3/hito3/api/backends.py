from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import Usuario

class RUTAuthenticationBackend(BaseBackend):
    def authenticate(self, request, rut=None, rut_personal=None, password=None):
        try:
            user = Usuario.objects.get(rut=rut, rut_personal=rut_personal)
            if user.check_password(password):
                return user
        except Usuario.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None
