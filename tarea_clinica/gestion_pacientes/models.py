from django.db import models


class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    registro_medico = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Dr(a). {self.nombre} - {self.especialidad}"


class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    fecha_nacimiento = models.DateField()
    medico_asignado = models.ForeignKey(Medico, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - RUT: {self.rut}"
