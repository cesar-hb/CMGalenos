from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Especialidad(models.Model):
    idEspecialidad = models.IntegerField(primary_key=True, verbose_name="Id especialidad")
    nombreEspecialidad = models.CharField(max_length=80, blank=False, null=False, verbose_name="Especialidad")

def __str__(self):
    return f"{self.idEspecialidad} - {self.nombreEspecialidad}"

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=80, blank=True, null=True, verbose_name="Rut")
    direccion = models.CharField(max_length=80, blank=True, null=True, verbose_name="Dirección")
    rol = models.CharField(max_length=1, blank=True, null=True, verbose_name="Rol")
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.user.email}) {self.user.rol}"

class AtencionMedica(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="ID")
    fecha = models.CharField(max_length=80, blank=False, null=False, verbose_name="Fecha atención")
    doctor = models.CharField(max_length=200, null=True, blank=True, verbose_name="Doctor a cargo")
    precio = models.IntegerField(blank=False, null=False, verbose_name="Precio")
    especialidad = models.ForeignKey(Especialidad, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.id
