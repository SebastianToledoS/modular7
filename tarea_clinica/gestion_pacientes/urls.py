from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pacientes, name='lista_pacientes'),
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('pacientes/nuevo/', views.crear_paciente, name='crear_paciente'),

    # Nuevas rutas para el CRUD completo:
    path('medicos/nuevo/', views.crear_medico, name='crear_medico'),
    path('pacientes/editar/<int:id>/',
         views.editar_paciente, name='editar_paciente'),
    path('medicos/editar/<int:id>/', views.editar_medico, name='editar_medico'),
]
