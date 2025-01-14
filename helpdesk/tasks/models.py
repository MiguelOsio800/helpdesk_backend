# tasks/models.py  
from django.db import models  
from usuarios.models import Usuario, Area  

class Prioridad(models.Model):  
    nivel = models.CharField(max_length=20, unique=True)  # Campo de texto para nivel de prioridad  

    def __str__(self):  
        return self.nivel 
    
    class Meta:
        verbose_name_plural = "Prioridad"

class Status(models.Model):  
    estado = models.CharField(max_length=20, unique=True)  # Campo de texto para estado  

    def __str__(self):  
        return self.estado  
    class Meta:
        verbose_name_plural = "Status"
class Task(models.Model):  
    incidencia = models.CharField(max_length=200)  
    descripcion = models.TextField()  
    area = models.ForeignKey(Area, on_delete=models.CASCADE)  
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  
    tecnicos = models.ManyToManyField(Usuario, related_name='tecnico_tasks', blank=True) 
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)  # Relación a Status  
    prioridad = models.ForeignKey(Prioridad, on_delete=models.SET_NULL, null=True, blank=True)  # Relación a Prioridad  

    def __str__(self):  
        return self.incidencia
    
    def save(self, *args, **kwargs):
        if not self.status:  # Si no se proporciona un estado
            pendiente_status, created = Status.objects.get_or_create(estado="Pendiente")
            self.status = pendiente_status  # Asignar el estado "Pendiente"
        super().save(*args, **kwargs)  # Llamar al método save original

    class Meta:
        verbose_name_plural = "Task"
