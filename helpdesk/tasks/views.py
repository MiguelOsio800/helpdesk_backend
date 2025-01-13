# tasks/views.py  
from rest_framework import viewsets  
from .models import Task, Prioridad, Status  
from .serializers import TaskSerializer, PrioridadSerializer, StatusSerializer  

class TaskViewSet(viewsets.ModelViewSet):  
    queryset = Task.objects.all()  
    serializer_class = TaskSerializer  

class PrioridadViewSet(viewsets.ModelViewSet):  
    queryset = Prioridad.objects.all()  
    serializer_class = PrioridadSerializer  

class StatusViewSet(viewsets.ModelViewSet):  
    queryset = Status.objects.all()  
    serializer_class = StatusSerializer