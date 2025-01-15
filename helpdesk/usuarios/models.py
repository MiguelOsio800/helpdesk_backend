# usuarios/models.py  
from django.db import models  
from django.contrib.auth.models import AbstractUser  

# ================================  
#           MODELO: AREA  
# ================================  

class Area(models.Model):  
    """Modelo que representa las áreas en la organización."""  
    nombre = models.CharField(max_length=100)  

    def __str__(self):  
        """Devuelve una representación legible del nombre del área."""  
        return self.nombre  

    class Meta:  
        verbose_name_plural = "Area"  


# ================================  
#           MODELO: ROL  
# ================================  

class Rol(models.Model):  
    """Modelo que representa los roles que un usuario puede tener."""  
    nombre = models.CharField(max_length=50, unique=True)  

    def __str__(self):  
        """Devuelve una representación legible del nombre del rol."""  
        return self.nombre  

    class Meta:  
        verbose_name_plural = "Rol"  


# ================================  
#       MODELO: USUARIO  
# ================================  

class Usuario(AbstractUser):  
    """Modelo que representa a los usuarios en el sistema, extendiendo AbstractUser para incluir área y rol."""  
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='usuarios', null=True)  # Relación con Área  
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name='usuarios', null=True)  # Relación con Rol  

    def __str__(self):  
        """Devuelve una representación legible del usuario, incluyendo su nombre y rol."""  
        return f"{self.first_name} {self.last_name} - {self.rol.nombre if self.rol else 'Sin rol'}"  

    class Meta:  
        verbose_name_plural = "Usuario"