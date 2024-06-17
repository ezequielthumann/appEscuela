from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Novedad 
# Create your views here.

def home(request):
    novedades = Novedad.objects.all()
    
    return render(
        request, 
        'index.html', 
        {
            'title': 'Home',
            'novedades': novedades,
        }
    )

def calendario(request):
    return render(
        request, 'calendario.html',
        {
        'title': 'calendario'
        }
    )

def clases_de_consulta(request):
    return render(
        request, 'clases consulta.html',
        {
        'title': 'clases de consulta'
        }
    )

def clases(request):
    return render(
        request, 'clases.html',
        {
            'title' : 'clases'
        }
    )

def planillas(request):
    return render(
        request, 'planillas.html',
        {
            'title': 'planillas'
        }
    )

def programas(request):
    return render(
        request, 'programas.html',
        {
            'title': 'programas'
        }
    )

def horarios(request):
    return render(
        request, 'horarios.html',
        {
            'title' : 'horarios'
        }
    )

def mesas_de_examen(request):
    return render(
        request, 'mesas examen.html',
        {
            'title' : 'mesas_de_examen'
        } 
    )

def novedad_detalle(request, novedad_id):
    novedad = get_object_or_404(Novedad, pk=novedad_id)
    return render(request, 'novedad', {'novedad': novedad, 'title': 'novedad'})