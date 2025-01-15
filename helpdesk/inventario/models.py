# inventario/models.py  
from django.db import models  
from usuarios.models import Usuario  
from tasks.models import Clasificacion  # Importa Clasificacion desde la app de tasks  

# ================================  
#         MODELO: TIPO EQUIPO  
# ================================  

class TipoEquipo(models.Model):  
    """Modelo que representa los diferentes tipos de equipos."""  
    nombre = models.CharField(max_length=100, unique=True)  

    def __str__(self):  
        """Devuelve una representación legible del tipo de equipo."""  
        return self.nombre  

    class Meta:  
        verbose_name_plural = "Tipos de Equipos"  


# ================================  
#         MODELO: NUMERO BIEN  
# ================================  

class NumeroBien(models.Model):  
    """Modelo que representa el número único asignado a un bien."""  
    numero = models.CharField(max_length=50, unique=True)  # Cambia max_length si es necesario  

    def __str__(self):  
        """Devuelve una representación legible del número de bien."""  
        return self.numero  

    class Meta:  
        verbose_name_plural = "Números de Bienes"  


# ================================  
#         MODELO: EQUIPO  
# ================================  

class Equipo(models.Model):  
    """Modelo que representa un equipo, que puede estar asignado a un usuario y tener un número único."""  
    tipo = models.ForeignKey(TipoEquipo, on_delete=models.CASCADE, related_name='equipos')  # Relación con TipoEquipo  
    usuario_asignado = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)  # Relación con Usuario  
    numero_bien = models.OneToOneField(NumeroBien, on_delete=models.CASCADE, related_name='equipo', null=True)  # Relación con NumeroBien  

    def __str__(self):  
        """Devuelve una representación legible del equipo. Debe tener un nombre definido en el modelo."""  
        return self.numero_bien.numero if self.numero_bien else "Equipo sin número"  

    class Meta:  
        verbose_name_plural = "Equipos"