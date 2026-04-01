from .forms import PacienteForm, MedicoForm
from .models import Paciente, Medico
from django.shortcuts import render, redirect, get_object_or_404
from .models import Medico, Paciente
from .forms import MedicoForm, PacienteForm


def lista_pacientes(request):
    busqueda = request.GET.get('nombre', '')
    if busqueda:
        # Uso de filtro ORM 'icontains' para buscar por nombre
        pacientes = Paciente.objects.filter(nombre__icontains=busqueda)
    else:
        pacientes = Paciente.objects.all()

    return render(request, 'gestion_pacientes/lista_pacientes.html', {'pacientes': pacientes})

# Crear un nuevo paciente


def crear_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'gestion_pacientes/formulario_paciente.html', {'form': form})


# 1. Función para CREAR Médico
def crear_medico(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = MedicoForm()
    return render(request, 'gestion_pacientes/formulario_medico.html', {'form': form})

# 2. Función para EDITAR Paciente


def editar_paciente(request, id):
    # Busca el paciente por su ID
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == 'POST':
        # Llena el formulario con los datos actuales
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'gestion_pacientes/formulario_paciente.html', {'form': form, 'titulo': 'Editar Paciente'})

# 3. Función para EDITAR Médico


def editar_medico(request, id):
    medico = get_object_or_404(Medico, id=id)
    if request.method == 'POST':
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = MedicoForm(instance=medico)
    return render(request, 'gestion_pacientes/formulario_medico.html', {'form': form, 'titulo': 'Editar Médico'})
