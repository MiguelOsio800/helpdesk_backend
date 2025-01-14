from django.db import models  
from django.contrib.auth.models import AbstractUser

class Area(models.Model):  
    nombre = models.CharField(max_length=100)  

    def __str__(self):  
        return self.nombre  
    
    class Meta:
        verbose_name_plural = "Area"

class Rol(models.Model):  
    nombre = models.CharField(max_length=50, unique=True)  

    def __str__(self):  
        return self.nombre  
    
    class Meta:
        verbose_name_plural = "Rol"

class Usuario(AbstractUser):  
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='usuarios', null=True)  # Relación con Area  
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name='usuarios',null=True)  # Relación con Rol  

    def __str__(self):  
        return f"{self.first_name} {self.last_name} - {self.rol.nombre if self.rol else "Sin rol"}"
    
    class Meta:
        verbose_name_plural = "Usuario"