# Generated by Django 5.0.4 on 2024-07-29 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_rename_nombre_exalumno_apellidos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exalumno',
            name='correo',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exalumno',
            name='tipo_trabajo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
