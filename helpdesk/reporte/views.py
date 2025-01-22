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

@api_view(['GET', 'POST'])  
def completar_informe(request, task_id):  
    """  
    Vista para completar un informe asociado a una tarea específica.  
    Solo permite que los usuarios en el área de 'tecnología' y con rol de 'técnico' completen el informe.  
    """  
    # Busca la tarea asociada, o lanza un error 404 si no existe.  
    task = get_object_or_404(Task, id=task_id)  

    # Verifica si el usuario pertenece al área de 'tecnología' y tiene el rol de 'técnico'  
    if request.user.area.nombre != 'tecnología' or request.user.rol.nombre != 'técnico':  
        return Response({'detail': 'No tienes permiso para completar este informe.'},  
                        status=status.HTTP_403_FORBIDDEN)  

    # Obtiene el informe asociado al usuario actual en el área de tecnología  
    informe = task.reporte_informes.filter(usuario=request.user).first()  

    # Si no se encuentra un informe para el usuario, devolver un error.  
    if informe is None:  
        return Response({'detail': 'Informe no encontrado o no autorizado'},   
                        status=status.HTTP_404_NOT_FOUND)  

    if request.method == 'POST':  
        serializer = InformeSerializer(informe, data=request.data)  
        if serializer.is_valid():  
            serializer.save()  

            # Verifica y actualiza el estado de la tarea tras guardar el informe.  
            check_and_update_task_status(task)  

            return Response(serializer.data, status=status.HTTP_200_OK)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
    # Si el método es GET, devuelve el informe serializado.  
    serializer = InformeSerializer(informe)  
    return Response(serializer.data)  

def check_and_update_task_status(task):  
    """Verifica si todos los informes asociados a la tarea están completos   
    y actualiza el estado de la tarea."""  
    informes = Informe.objects.filter(task=task)  

    # Comprobar si todos los informes están completos  
    if all(informe.completado for informe in informes):  
        finalizado_status, created = Status.objects.get_or_create(estado="Finalizado")  # Obtiene o crea el estado "Finalizado"  
        task.status = finalizado_status  
        task.save()