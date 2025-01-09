# models.py  
from django.db import models  

class Area(models.Model):  
    nombre = models.CharField(max_length=100)  

    def __str__(self):  
        return self.nombre  

class Usuario(models.Model):  
    ROL_CHOICES = [  
        ('tecnico', 'Técnico'),  
        ('administrador', 'Administrador'),  
        ('usuario', 'Usuario'),  
    ]  

    nombres = models.CharField(max_length=50)  
    apellidos = models.CharField(max_length=50)  
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='usuarios')  # Relación con Area  
    correo = models.EmailField(unique=True)  
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)  # Opciones para el rol  

    def __str__(self):  
        return f"{self.nombres} {self.apellidos} - {self.rol}"