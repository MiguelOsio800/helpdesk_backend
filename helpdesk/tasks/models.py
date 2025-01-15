# tasks/models.py  
from django.db import models  
from usuarios.models import Usuario, Area  

# ================================  
#           MODELO: PRIORIDAD  
# ================================  

class Prioridad(models.Model):  
    """Modelo que representa las prioridades de las tareas."""  
    nivel = models.CharField(max_length=20, unique=True)  

    def __str__(self):  
        """Devuelve una representación legible de la prioridad."""  
        return self.nivel  

    class Meta:  
        verbose_name_plural = "Prioridades"  


# ================================  
#           MODELO: STATUS  
# ================================  

class Status(models.Model):  
    """Modelo que representa los estados de las tareas."""  
    estado = models.CharField(max_length=20, unique=True)  

    def __str__(self):  
        """Devuelve una representación legible del estado."""  
        return self.estado  

    class Meta:  
        verbose_name_plural = "Status"  


# ================================  
#       MODELO: CLASIFICACION  
# ================================  

class Clasificacion(models.Model):  
    """Modelo que representa las clasificaciones de las incidencias."""  
    nombre_clasificacion = models.CharField(max_length=200, unique=True)  

    def __str__(self):  
        """Devuelve una representación legible de la clasificación."""  
        return self.nombre_clasificacion  

    class Meta:  
        verbose_name_plural = "Clasificaciones"  


# ================================  
#           MODELO: TASK  
# ================================  

class Task(models.Model):  
    """Modelo que representa una tarea o incidencia."""  
    incidencia = models.CharField(max_length=200)  
    descripcion = models.TextField()  
    area = models.ForeignKey(Area, on_delete=models.CASCADE)  
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  
    tecnicos = models.ManyToManyField(Usuario, related_name='tecnico_tasks', blank=True)  
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)  
    prioridad = models.ForeignKey(Prioridad, on_delete=models.SET_NULL, null=True, blank=True)  
    fecha_creacion = models.DateField(null=True, blank=True)  
    fecha_final = models.DateField(null=True, blank=True)  

    def __str__(self):  
        """Devuelve una representación legible de la tarea."""  
        return self.incidencia  

    def save(self, *args, **kwargs):  
        """Método para guardar la tarea. Establece el estado a 'Pendiente' si no se ha asignado ningún estado.  
        
        Args:  
            *args: Posicionales que se pasan a la superclase (Modelo).  
            **kwargs: Palabras clave que se pasan a la superclase (Modelo).  
        """  
        if not self.status:  
            pendiente_status, created = Status.objects.get_or_create(estado="Pendiente")  
            self.status = pendiente_status  
        super().save(*args, **kwargs)  

    class Meta:  
        verbose_name_plural = "Tasks"