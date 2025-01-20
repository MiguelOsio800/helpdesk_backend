# tasks/views.py  

from rest_framework import viewsets  
from rest_framework.decorators import action  
from rest_framework.response import Response  
from .models import Task, Prioridad, Status, Clasificacion  
from .serializers import TaskSerializer, PrioridadSerializer, StatusSerializer, ClasificacionSerializer  

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