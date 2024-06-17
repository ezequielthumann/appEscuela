from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('/calendario', views.calendario, name='calendario'),
    path('/clase consulta', views.clases_de_consulta, name='clases de consulta'),
    path('/clases', views.clases, name='clases'),
    path('/planillas', views.planillas, name='planillas'),
    path('/programas', views.programas, name="programas"),
    path('/horarios', views.horarios, name="horarios"),
    path('/mesas de examen', views.mesas_de_examen, name="mesas de examen"),
    path('novedad/<int:novedad_id>/', views.novedad_detalle, name='novedad_detalle'),
]