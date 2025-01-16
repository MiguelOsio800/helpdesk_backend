from django.db import models  
from django.contrib.auth.models import AbstractUser  
from django.contrib.auth.hashers import make_password  

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
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='usuarios', null=True)  
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name='usuarios', null=True)  
    password = models.CharField(max_length=128, default=make_password('default_password'))  
    username = models.CharField(max_length=150, unique=True, default='default_username')  

    def __str__(self):  
        return f"{self.first_name} {self.last_name} - {self.rol.nombre if self.rol else 'Sin rol'}"  

    class Meta:  
        verbose_name_plural = "Usuario"  

class Clasificacion(models.Model):  
    nombre = models.CharField(max_length=100)  

    def __str__(self):  
        return self.nombre  
    
    class Meta:  
        verbose_name_plural = "Clasificacion"  

class Task(models.Model):  
    titulo = models.CharField(max_length=200)  
    clasificacion = models.ForeignKey(Clasificacion, on_delete=models.CASCADE, related_name='tasks')  
    usuario_asignado = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tasks')  

    def __str__(self):  
        return f"{self.titulo} - {self.clasificacion.nombre if self.clasificacion else 'Sin clasificacion'}"  

    class Meta:  
        verbose_name_plural = "Task"