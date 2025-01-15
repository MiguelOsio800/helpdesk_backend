# tasks/serializers.py  
from rest_framework import serializers  
from django.contrib.auth.models import User  # Importamos el modelo User  
from .models import Task, Prioridad, Status, Clasificacion  # Manteniendo otras importaciones  

class UserSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = User  
        fields = ['username']  # Solo retorna el campo username  

class PrioridadSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Prioridad  
        fields = '__all__'  

class StatusSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Status  
        fields = '__all__'  

class ClasificacionSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Clasificacion  
        fields = '__all__'  

class TaskSerializer(serializers.ModelSerializer):  
    # Cambiar este campo para utilizar el serializador correcto  
    usuario = UserSerializer(read_only=True)  # Utiliza el serializador User para el campo usuario  
    tecnicos = UserSerializer(many=True, read_only=True)  # Suponiendo que la tarea puede tener varios técnicos asignados (ManyToMany)  

    class Meta:  
        model = Task  
        fields = ['incidencia', 'descripcion', 'area', 'usuario', 'tecnicos', 'status', 'prioridad', 'fecha_creacion', 'fecha_final']  # Especifica los campos deseados