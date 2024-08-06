from django_cron import CronJobBase, Schedule
from .models import ExAlumno
from .views import realizar_busqueda  # Importa la función de views.py
import logging

# Configuración del logger
logger = logging.getLogger(__name__)

class ActualizarDatosExAlumnosCronJob(CronJobBase):
    RUN_EVERY_MINS = 1  # Ejecuta cada 1 minuto para pruebas

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'mi_app.actualizar_datos_exalumnos_cron_job'  # Un código único para este trabajo cron

    def do(self):
        logger.info("Ejecutando el trabajo cron para actualizar datos de exalumnos")
        
        # Filtra los exalumnos a los que se les quiere hacer seguimiento
        exalumnos = ExAlumno.objects.all()

        for exalumno in exalumnos:
            try:
                # Realiza la búsqueda y actualiza los datos del exalumno
                resultados = realizar_busqueda(
                    nombre=exalumno.nombres,
                    profesion=exalumno.profesion,
                    ciudad=exalumno.ciudad,
                    region=exalumno.region,
                    correo=exalumno.correo,
                    browser='chrome'  # Puedes cambiar el navegador si es necesario
                )
                
                # Aquí puedes actualizar el modelo ExAlumno con los nuevos datos obtenidos
                if resultados:
                    for res in resultados:
                        # Puedes actualizar otros campos de ExAlumno según lo necesites
                        exalumno.link = res['link']
                        exalumno.save()

            except Exception as e:
                logger.error(f"Error al actualizar datos de {exalumno.nombres}: {e}")
        
        logger.info("El trabajo cron se ejecutó correctamente")
