# Generated by Django 5.0.4 on 2024-07-22 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_exalumno_delete_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exalumno',
            old_name='ciudad',
            new_name='ciudad_desempeno',
        ),
        migrations.RenameField(
            model_name='exalumno',
            old_name='tipo_de_trabajo',
            new_name='tipo_trabajo',
        ),
        migrations.RemoveField(
            model_name='exalumno',
            name='whatsapp',
        ),
        migrations.AlterField(
            model_name='exalumno',
            name='correo_electronico',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='exalumno',
            name='cuenta_rrss',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exalumno',
            name='telefono',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
