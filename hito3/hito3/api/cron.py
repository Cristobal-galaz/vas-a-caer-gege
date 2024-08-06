from django_cron import CronJobBase, Schedule
from .models import ExAlumno
from .scraping import actualizar_datos_exalumnos  # Asegúrate de tener esta función en tu código

class ActualizarDatosExAlumnosCronJob(CronJobBase):
    RUN_EVERY_MINS = 1440  # 24 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'your_app.actualizar_datos_exalumnos_cron_job'  # Un código único para este trabajo cron

    def do(self):
        actualizar_datos_exalumnos()
