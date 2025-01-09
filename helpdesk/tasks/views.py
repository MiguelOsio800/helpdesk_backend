from rest_framework import viewsets  
from .models import Task  # Asegúrate de que estás importando Task aquí  
from .serializers import TaskSerializer  # Importar el serializador de Task  

class TaskViewSet(viewsets.ModelViewSet):  
    queryset = Task.objects.all()  
    serializer_class = TaskSerializer