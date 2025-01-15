# inventario/models.py  
from django.db import models  
from usuarios.models import Usuario  
from tasks.models import Clasificacion  # Importa Clasificacion desde la app de tasks  

class TipoEquipo(models.Model):  
    nombre = models.CharField(max_length=100, unique=True)  

    def __str__(self):  
        return self.nombre  

    class Meta:  
        verbose_name_plural = "Tipos de Equipos"  

class Equipo(models.Model):  
    tipo = models.ForeignKey(TipoEquipo, on_delete=models.CASCADE, related_name='equipos')  
    usuario_asignado = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)  
    numero_bien = models.OneToOneField('NumeroBien', on_delete=models.CASCADE, related_name='equipo', null=True)  

    def __str__(self):  
        return self.nombre  

    class Meta:  
        verbose_name_plural = "Equipos"  

class NumeroBien(models.Model):  
    numero = models.CharField(max_length=50, unique=True)  # Cambia max_length si es necesario  
   
    def __str__(self):  
        return self.numero  

    class Meta:  
        verbose_name_plural = "Números de Bienes"