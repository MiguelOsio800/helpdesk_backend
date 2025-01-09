# tasks/views.py  
from rest_framework import viewsets  
from .models import Task  # Asegúrate de tener este modelo definido  
from .serializers import TaskSerializer  # Asegúrate de tener este serializer definido  

class TaskViewSet(viewsets.ModelViewSet):  
    queryset = Task.objects.all()  # Esto obtiene todos los objetos de Task de la base de datos  
    serializer_class = TaskSerializer  # Especifica el serializer para convertir el modelo a JSON