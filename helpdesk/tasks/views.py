# tasks/views.py  

from rest_framework import viewsets  
from rest_framework.decorators import action  
from rest_framework.response import Response  
from .models import Task, Prioridad, Status, Clasificacion  
from .serializers import TaskSerializer, PrioridadSerializer, StatusSerializer, ClasificacionSerializer  
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Task, Informe
from .serializers import InformeSerializer

###############################################################################  
### ViewSet para la clase Task que maneja las tareas del sistema          ###  
###############################################################################  
class TaskViewSet(viewsets.ModelViewSet):  
    queryset = Task.objects.all()  # Consulta para obtener todas las instancias de Task  
    serializer_class = TaskSerializer  # Serializador asociado con el modelo Task  

    # Nueva acción personalizada para actualizar solo ciertos campos de Task  
    @action(detail=True, methods=['put'], url_path='update-technical-status-classification')  
    def update_technical_status_classification(self, request, pk=None):  
        """  
        Método para actualizar solo los campos 'tecnicos', 'status' y 'clasificacion'   
        de una tarea específica.  

        :param request: Objeto de solicitud que contiene los datos para la actualización.  
        :param pk: Clave primaria de la tarea que se va a actualizar.  
        :return: Respuesta con los datos actualizados o errores de validación.  
        """  
        task = self.get_object()  # Obtiene la instancia de Task mediante la clave primaria  
        serializer = self.get_serializer(task, data=request.data, partial=True)  # Permite actualizaciones parciales  

        if serializer.is_valid():  
            serializer.save()  # Guarda los cambios en la base de datos  
            return Response(serializer.data)  # Devuelve los datos actualizados  

        return Response(serializer.errors, status=400)  # Devuelve errores si la validación falla  


###############################################################################  
### ViewSet para manejar las prioridades en el sistema                      ###  
###############################################################################  
class PrioridadViewSet(viewsets.ModelViewSet):  
    queryset = Prioridad.objects.all()  # Consulta para obtener todas las instancias de Prioridad  
    serializer_class = PrioridadSerializer  # Serializador asociado con el modelo Prioridad  


###############################################################################  
### ViewSet para manejar los estados en el sistema                          ###  
###############################################################################  
class StatusViewSet(viewsets.ModelViewSet):  
    queryset = Status.objects.all()  # Consulta para obtener todas las instancias de Status  
    serializer_class = StatusSerializer  # Serializador asociado con el modelo Status  


###############################################################################  
### ViewSet para manejar las clasificaciones en el sistema                  ###  
###############################################################################  
class ClasificacionViewSet(viewsets.ModelViewSet):  
    queryset = Clasificacion.objects.all()  # Consulta para obtener todas las instancias de Clasificacion  
    serializer_class = ClasificacionSerializer  # Serializador asociado con el modelo Clasificacion

class InformeViewSet(viewsets.ModelViewSet):
    queryset = Informe.objects.all()
    serializer_class = InformeSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        task_id = self.request.query_params.get('task_id')
        if task_id:
            queryset = queryset.filter(task_id=task_id)
        return queryset


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

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

@api_view(['GET', 'POST'])
def completar_informe(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    informes = task.informes.order_by('id')
    informe_completado = False

    for informe in informes:
        if informe.usuario == request.user:
            if informe_completado:
                if request.method == 'POST':
                    serializer = InformeSerializer(informe, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_200_OK)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    serializer = InformeSerializer(informe)
                return Response(serializer.data)
            else:
                informe_completado = informe.completado
    return Response({'detail': 'Informe no encontrado o no autorizado'}, status=status.HTTP_404_NOT_FOUND)
