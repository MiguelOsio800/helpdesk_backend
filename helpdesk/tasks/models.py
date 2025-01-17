#############################################  
##### Modelos para el Sistema de Tareas #####  
#############################################  

from django.db import models  # Importamos el módulo models de Django  
from django.utils import timezone  # Importa timezone para obtener la hora actual  
from usuarios.models import Usuario, Area  # Importamos los modelos Usuario y Area  

#################################  
##### Clase Prioridad ###########  
#################################  
class Prioridad(models.Model):  
    nivel = models.CharField(max_length=20, unique=True)  # Campo para el nivel de prioridad  

    def __str__(self):  
        return self.nivel  # Representación en cadena del objeto  

    class Meta:  
        verbose_name_plural = "Prioridad"  # Nombre plural en el panel de administración  

#################################
##### Clase Status ##############  
#################################
class Status(models.Model):  
    estado = models.CharField(max_length=20, unique=True)  # Campo para el estado de la tarea  

    def __str__(self):  
        return self.estado  # Representación en cadena del objeto  

    class Meta:  
        verbose_name_plural = "Status"  # Nombre plural en el panel de administración  

#########################################
##### Clase Clasificacion ###############  
#########################################
class Clasificacion(models.Model):  
    clasificacion = models.CharField(max_length=200, unique=True)  # Campo para la clasificación  

    def __str__(self):  
        return self.clasificacion  # Representación en cadena del objeto  

    class Meta:  
        verbose_name_plural = "Clasificaciones"  # Nombre plural en el panel de administración  

##################################  
##### Clase Task #################  
##################################  

class Task(models.Model):  
    incidencia = models.CharField(max_length=200)  # Campo para la descripción de la incidencia  
    descripcion = models.TextField()  # Campo para la descripción detallada  
    area = models.ForeignKey(Area, on_delete=models.CASCADE)  # Relación con el modelo Area  
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Relación con el modelo Usuario  
    tecnicos = models.ManyToManyField(Usuario, related_name='tecnico_tasks', blank=True)  # Relación muchos a muchos con Usuario  
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)  # Relación con el modelo Status  
    prioridad = models.ForeignKey(Prioridad, on_delete=models.SET_NULL, null=True, blank=True)  # Relación con el modelo Prioridad  
    fecha_creacion = models.DateTimeField(null=True, blank=True)  # Campo para la fecha de creación (sin auto_now_add)  
    fecha_final = models.DateField(null=True, blank=True)  # Campo para la fecha final  
    clasificacion = models.ForeignKey(Clasificacion, on_delete=models.SET_NULL, null=True, blank=True)  # Relación con el modelo Clasificacion  

    def __str__(self):  
        return self.incidencia  # Representación en cadena del objeto  

    def save(self, *args, **kwargs):  
        # Establece el estado a "Pendiente" si no se ha asignado ninguno  
        if not self.status:  
            pendiente_status, created = Status.objects.get_or_create(estado="Pendiente")  
            self.status = pendiente_status  
        
        # Establece la fecha de creación si es una nueva instancia  
        if self.pk is None:  # Verifica si es un nuevo objeto (sin ID)  
            self.fecha_creacion = timezone.now()  # Asigna la fecha y hora actuales  
        
        super().save(*args, **kwargs)  # Llama al método save de la clase padre  

    class Meta:  
        verbose_name_plural = "Task"  # Nombre plural en el panel de administración