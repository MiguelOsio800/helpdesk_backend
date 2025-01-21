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
    incidencia = models.CharField(max_length=200)
    descripcion = models.TextField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tecnicos = models.ManyToManyField(Usuario, related_name='tecnico_tasks', blank=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)
    prioridad = models.ForeignKey(Prioridad, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_creacion = models.DateTimeField(null=True, blank=True)
    fecha_final = models.DateField(null=True, blank=True)
    clasificacion = models.ForeignKey(Clasificacion, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.incidencia

    def save(self, *args, **kwargs):
        if not self.status:
            pendiente_status, created = Status.objects.get_or_create(estado="Pendiente")
            self.status = pendiente_status

        if self.pk is None:
            self.fecha_creacion = timezone.now()

        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Task"

class Informe(models.Model):
    task = models.ForeignKey(Task, related_name='informes', on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    equipo = models.CharField(max_length=200)
    numero_de_bien = models.CharField(max_length=100)
    motivo = models.TextField()
    solucion = models.TextField()
    status = models.CharField(max_length=100)  # Cambiado a CharField
    observacion = models.TextField()
    completado = models.BooleanField(default=False)

    def __str__(self):
        return f'Informe de {self.usuario} para {self.task}'
