# tasks/serializers.py  
from rest_framework import serializers  
from .models import Task  

class TaskSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Task  # Modelo que estás serializando  
        fields = '__all__'  # O puedes especificar campos específicos, por ejemplo: ['id', 'title', 'description', 'completed']