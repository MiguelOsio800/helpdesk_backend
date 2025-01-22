from django.db import models
from tasks.models import Task  # Importa el modelo Task si lo necesitas
from usuarios.models import Usuario, Area  # Importa Usuario y Area si son necesarios


class Informe(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)  # Cambiado related_name
    area = models.ForeignKey(Area, on_delete=models.CASCADE)  # Cambiado related_name
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Cambiado related_name
    equipo = models.CharField(max_length=200)
    numero_de_bien = models.CharField(max_length=100)
    solucion = models.TextField()
    observacion = models.TextField()
    completado = models.BooleanField(default=False)

    def __str__(self):
        return f'Informe de {self.usuario} para {self.task}'

    class Meta:
        verbose_name_plural = "Informes"
