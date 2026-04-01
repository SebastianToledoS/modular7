from django.test import TestCase
from .models import Medico, Paciente


class MedicoTest(TestCase):
    def setUp(self):
        # Configuramos un médico de prueba que no afectará tu base de datos real
        self.medico = Medico.objects.create(
            nombre="Dra. Ana Silva",
            especialidad="Neurología",
            registro_medico="MED-999"
        )

    def test_medico_validaciones(self):
        # Validación 1: ¿El objeto creado es realmente de la clase Medico?
        self.assertTrue(isinstance(self.medico, Medico))

        # Validación 2: ¿El nombre se guardó exactamente como lo escribimos?
        self.assertEqual(self.medico.nombre, "Dra. Ana Silva")

        # Validación 3: ¿La especialidad es la correcta?
        self.assertEqual(self.medico.especialidad, "Neurología")


class PacienteTest(TestCase):
    def setUp(self):
        # Para crear un paciente, primero necesitamos un médico asignado
        self.medico = Medico.objects.create(
            nombre="Dr. Pedro Soto",
            especialidad="Pediatría",
            registro_medico="MED-888"
        )
        self.paciente = Paciente.objects.create(
            nombre="Carlos Pinto",
            rut="19876543-2",
            fecha_nacimiento="1995-05-15",
            medico_asignado=self.medico
        )

    def test_paciente_validaciones(self):
        # Validación 1: ¿Hay exactamente 1 paciente en nuestra base de datos de prueba?
        self.assertEqual(Paciente.objects.count(), 1)

        # Validación 2: ¿El RUT coincide con el que ingresamos?
        self.assertEqual(self.paciente.rut, "19876543-2")

        # Validación 3: ¿El médico asignado a Carlos es el Dr. Pedro Soto?
        self.assertEqual(self.paciente.medico_asignado.nombre,
                         "Dr. Pedro Soto")
