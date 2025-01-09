# tasks/serializers.py  
from rest_framework import serializers  
from .models import Task, Prioridad, Status  # Cambiar 'Estado' a 'Status'  

class PrioridadSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Prioridad  
        fields = '__all__'  

class StatusSerializer(serializers.ModelSerializer):  # Cambiar 'EstadoSerializer' a 'StatusSerializer'  
    class Meta:  
        model = Status  
        fields = '__all__'  

class TaskSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Task  
        fields = '__all__'