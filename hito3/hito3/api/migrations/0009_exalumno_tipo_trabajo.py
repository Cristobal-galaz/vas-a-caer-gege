# Generated by Django 5.0.4 on 2024-07-29 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_rename_contacto_exalumno_correo'),
    ]

    operations = [
        migrations.AddField(
            model_name='exalumno',
            name='tipo_trabajo',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
