# Generated by Django 5.0.4 on 2024-06-17 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0002_novedad_fecha_publicacion_novedad_imagen_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='novedad',
            name='imagen',
        ),
    ]
