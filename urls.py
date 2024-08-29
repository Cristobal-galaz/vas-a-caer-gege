
from .views import user_login, user_login_success
from django.urls import path
from . import views
from .views import logout_view

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),  # Ruta para la página principal
    path('login/', views.user_login, name='user_login'),  # Ruta para el inicio de sesión
    path('registre/', views.register_user, name='user_register'),  # Ruta para el registro de usuarios
    path('registre/<str:username>/', views.registration_success, name='registration_success'),  # Ruta para la página de éxito
    path('logout/', logout_view, name='user_logout'),
    path('login/success/', views.user_login_success, name='user_login_success'),
]