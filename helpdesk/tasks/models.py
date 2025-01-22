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
        verbose_name_plural = "Prioridades"  # Nombre plural en el panel de administración  

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
    incidencia = models.CharField(max_length=200)  # Campo para la incidencia  
    descripcion = models.TextField()  # Campo para la descripción  
    area = models.ForeignKey(Area, on_delete=models.CASCADE)  # Campo para el área  
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Campo para el usuario  
    tecnicos = models.ManyToManyField(Usuario, related_name='tecnico_tasks', blank=True)  # Campo para los técnicos  
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)  # Campo para el estado  
    prioridad = models.ForeignKey(Prioridad, on_delete=models.SET_NULL, null=True, blank=True)  # Campo para la prioridad  
    fecha_creacion = models.DateTimeField(null=True, blank=True)  # Campo para la fecha de creación  
    fecha_final = models.DateField(null=True, blank=True)  # Campo para la fecha final  
    clasificacion = models.ForeignKey(Clasificacion, on_delete=models.SET_NULL, null=True, blank=True)  # Campo para la clasificación  

    def __str__(self):  
        return self.incidencia  # Representación en cadena de la tarea  

    def save(self, *args, **kwargs):  
        if not self.status:  
            pendiente_status, created = Status.objects.get_or_create(estado="Pendiente")  
            self.status = pendiente_status  

        if self.pk is None:  
            self.fecha_creacion = timezone.now()  

        super().save(*args, **kwargs)  

    class Meta:  
        verbose_name_plural = "Tareas"  # Nombre plural en el panel de administración