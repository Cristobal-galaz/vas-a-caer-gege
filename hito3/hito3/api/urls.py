from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'exalumnos', views.ExAlumnoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('api/search/', views.search_exalumno, name='search_exalumno'),
    path('download_csv/', views.download_csv, name='download_csv'),
    path('api/', include(router.urls)),
]
