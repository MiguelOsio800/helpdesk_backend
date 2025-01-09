from django.db import models  
from usuarios.models import Usuario, Area  # Asegúrate de importar Area  


class Prioridad(models.Model):  
    NIVEL_PRIORIDAD = (  
        ('alta', 'Alta'),  
        ('normal', 'Normal'),  
        ('baja', 'Baja'),  
    )  

    nivel = models.CharField(max_length=20, choices=NIVEL_PRIORIDAD, unique=True)  

    def __str__(self):  
        return self.nivel  

class Task(models.Model):  
    ESTADOS = (  
        ('Finalizada', 'Finalizada'),  
        ('pendiente', 'Pendiente'),  
        ('en_proceso', 'En proceso'),  
    )  
    
    incidencia = models.CharField(max_length=200)  
    descripcion = models.TextField()  
    area = models.ForeignKey(Area, on_delete=models.CASCADE)  
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  
    tecnicos = models.ManyToManyField(Usuario, related_name='tecnico_tasks')  
    status = models.CharField(max_length=20, choices=ESTADOS)  
    prioridad = models.ForeignKey(Prioridad, on_delete=models.SET_NULL, null=True, blank=True)  # Relación a Prioridad  

    def __str__(self):  
        return self.incidencia 