from django.db import models  
from usuarios.models import Usuario, Area  

class Prioridad(models.Model):  
    nivel = models.CharField(max_length=20, unique=True)  

    def __str__(self):  
        return self.nivel   
    
    class Meta:  
        verbose_name_plural = "Prioridad"  

class Status(models.Model):  
    estado = models.CharField(max_length=20, unique=True)  

    def __str__(self):  
        return self.estado  
    
    class Meta:  
        verbose_name_plural = "Status"  

class Clasificacion(models.Model):  
    clasificacion = models.CharField(max_length=200, unique=True)  # Cambiar 'Clasificacion' a 'clasificacion' en minúsculas  

    def __str__(self):  
        return self.clasificacion  # Cambiar 'self.tema' a 'self.clasificacion'  

    class Meta:  
        verbose_name_plural = "Clasificaciones"  

class Task(models.Model):  
    incidencia = models.CharField(max_length=200)  
    descripcion = models.TextField()  
    area = models.ForeignKey(Area, on_delete=models.CASCADE)  
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  
    tecnicos = models.ManyToManyField(Usuario, related_name='tecnico_tasks', blank=True)   
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)  
    prioridad = models.ForeignKey(Prioridad, on_delete=models.SET_NULL, null=True, blank=True)  
    fecha_creacion = models.DateField(null=True, blank=True)  
    fecha_final = models.DateField(null=True, blank=True)  
    clasificacion = models.ForeignKey(Clasificacion, on_delete=models.SET_NULL, null=True, blank=True)  

    def __str__(self):  
        return self.incidencia  
    
    def save(self, *args, **kwargs):  
        if not self.status:  
            pendiente_status, created = Status.objects.get_or_create(estado="Pendiente")  
            self.status = pendiente_status  
        super().save(*args, **kwargs)  

    class Meta:  
        verbose_name_plural = "Task"