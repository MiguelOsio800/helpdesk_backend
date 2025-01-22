from rest_framework import viewsets, status  
from rest_framework.decorators import api_view  
from rest_framework.response import Response  
from django.shortcuts import get_object_or_404  
from .models import Informe  
from tasks.models import Task, Status  # Asegúrate de importar Status  
from .serializers import InformeSerializer  

class ReporteViewSet(viewsets.ModelViewSet):  
    queryset = Informe.objects.all()  
    serializer_class = InformeSerializer  

    def create(self, request, *args, **kwargs):
        print(request.data)
        consulta_tasks = Task.objects.filter(id=request.data['task'])
        print (consulta_tasks.values('tecnicos'))
        for tecnico in consulta_tasks.values('tecnicos'):
            print('tecnicos:',tecnico['tecnicos'])
            print('tasks:',request.data['task'])
            consulta_reporte = Informe.objects.filter(task=request.data['task'],usuario=tecnico['tecnicos'])
            print('consulta_reporte:',consulta_reporte)
            if consulta_reporte:
                print('Ya reporto')
            else:
                print('No reporto')  
           
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)