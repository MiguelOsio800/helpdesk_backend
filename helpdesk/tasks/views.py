from rest_framework import viewsets  
from rest_framework.decorators import action  
from rest_framework.response import Response  
from .models import Task, Prioridad, Status, Clasificacion  
from .serializers import TaskSerializer, PrioridadSerializer, StatusSerializer, ClasificacionSerializer  
from rest_framework.decorators import api_view  
from rest_framework import status  
from django.shortcuts import get_object_or_404  

class TaskViewSet(viewsets.ModelViewSet):  
    queryset = Task.objects.all()  
    serializer_class = TaskSerializer  

    @action(detail=True, methods=['put'], url_path='update-technical-status-classification')  
    def update_technical_status_classification(self, request, pk=None):  
        task = self.get_object()  
        serializer = self.get_serializer(task, data=request.data, partial=True)  

        if serializer.is_valid():  
            serializer.save()  
            return Response(serializer.data)  
        return Response(serializer.errors, status=400)  


class PrioridadViewSet(viewsets.ModelViewSet):  
    queryset = Prioridad.objects.all()  
    serializer_class = PrioridadSerializer  


class StatusViewSet(viewsets.ModelViewSet):  
    queryset = Status.objects.all()  
    serializer_class = StatusSerializer  


class ClasificacionViewSet(viewsets.ModelViewSet):  
    queryset = Clasificacion.objects.all()  
    serializer_class = ClasificacionSerializer

    @action(detail=True, methods=['put'], url_path='update-technical-status-classification')
    def update_technical_status_classification(self, request, pk=None):
        task = self.get_object()
        serializer = self.get_serializer(task, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            # Crear informes vacíos si se han asignado técnicos nuevos
            for tecnico in task.tecnicos.all():
                Informe.objects.get_or_create(task=task, usuario=tecnico, defaults={
                    'area': task.area,
                    'status': 'Pendiente'  # Status por defecto
                })
            return Response(serializer.data)
        return Response(serializer.errors, status=400)