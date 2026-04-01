from django import forms
from .models import Medico, Paciente


class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control'}),
            'registro_medico': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        # Aquí inyectamos Bootstrap a los inputs
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Juan Pérez'}),
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 12345678-9'}),
            # El type='date' activa el calendario automático del navegador
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'medico_asignado': forms.Select(attrs={'class': 'form-select'}),
        }
