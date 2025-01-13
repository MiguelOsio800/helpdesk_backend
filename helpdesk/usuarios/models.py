# models.py  
from django.db import models  

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

class Usuario(models.Model):  
    nombres = models.CharField(max_length=50)  
    apellidos = models.CharField(max_length=50)  
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='usuarios')  # Relación con Area  
    correo = models.EmailField(unique=True)  
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name='usuarios')  # Relación con Rol  

    def __str__(self):  
        return f"{self.nombres} {self.apellidos} - {self.rol.nombre}"
    
    class Meta:
        verbose_name_plural = "Usuario"