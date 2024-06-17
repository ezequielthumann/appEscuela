# Generated by Django 5.0.4 on 2024-06-17 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0003_remove_novedad_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novedad',
            name='tipo_imagen',
            field=models.CharField(choices=[('atencion', 'Imagen de atención'), ('coopedora', 'Imagen de Coopedaro'), ('matriculacion', 'Imagen de matriculación'), ('mesas_examen', 'Imagen de mesas de examen')], default='atencion', max_length=20),
        ),
    ]