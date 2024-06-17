from django.db import models
from django.utils import timezone

class Novedad(models.Model):
    OPCIONES_IMAGEN = [
        ('atencion', 'Imagen de atención'),
        ('coopedora', 'Imagen de Coopedaro'),
        ('matriculacion', 'Imagen de matriculación'),
        ('mesas_examen', 'Imagen de mesas de examen'),
    ]

    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    tipo_imagen = models.CharField(max_length=20, choices=OPCIONES_IMAGEN, default='atencion')
    fecha_publicacion = models.DateTimeField(default=timezone.now)