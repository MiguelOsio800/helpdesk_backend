#######################################################  
##### Vistas para el Sistema de Usuarios y Tareas #####  
#######################################################  

from rest_framework import viewsets  # Importamos el módulo viewsets de Django REST Framework  
from rest_framework.response import Response  # Importamos Response para devolver respuestas HTTP  
from .models import Usuario, Area, Rol, Clasificacion, Task  # Importamos los modelos necesarios  
from .serializers import UsuarioSerializer, AreaSerializer, RolSerializer, ClasificacionSerializer, TaskSerializer  # Importamos los serializadores  

##################################  
##### Clase UsuarioViewSet #######  
##################################  
class UsuarioViewSet(viewsets.ModelViewSet):  
    queryset = Usuario.objects.all()  # Consulta que obtiene todos los usuarios  
    serializer_class = UsuarioSerializer  # Serializador que transforma el modelo Usuario a JSON  

    def list(self, request, *args, **kwargs):  
        return super().list(request, *args, **kwargs)  # Devuelve todos los usuarios  

    def list_tecnicos(self, request, *args, **kwargs):  
        # Filtramos los usuarios que tienen rol técnico  
        rol_tecnico = Rol.objects.filter(nombre='tecnico').first()  # Asegúrate de que 'tecnico' es el nombre correcto del rol  
        if rol_tecnico:  
            usuarios_tecnicos = self.queryset.filter(rol=rol_tecnico)  # Filtramos los usuarios con rol técnico  
            serializer = self.get_serializer(usuarios_tecnicos, many=True)  # Serializamos los usuarios filtrados  
            return Response(serializer.data)  # Devolvemos los datos serializados  
        return Response([])  # Devuelve una lista vacía si no hay técnicos  
    
    def list_tecnologia(self, request, *args, **kwargs):  
        # Filtramos los usuarios que tienen el área tecnología  
        area_tecnologia = Area.objects.filter(nombre='Tecnologia').first()  # Asegúrate de que 'Tecnologia' es el nombre correcto del área  
        if area_tecnologia:  
            usuarios_tecnologia = self.queryset.filter(area=area_tecnologia)  # Filtramos los usuarios con área tecnología  
            serializer = self.get_serializer(usuarios_tecnologia, many=True)  # Serializamos los usuarios filtrados  
            return Response(serializer.data)  # Devolvemos los datos serializados  
        return Response([])  # Devuelve una lista vacía si no hay técnicos  

##################################  
##### Clase AreaViewSet ##########  
##################################  
class AreaViewSet(viewsets.ModelViewSet):  
    queryset = Area.objects.all()  # Consulta que obtiene todas las áreas  
    serializer_class = AreaSerializer  # Serializador que transforma el modelo Area a JSON  

##################################  
##### Clase RolViewSet ###########  
##################################  
class RolViewSet(viewsets.ModelViewSet):  
    queryset = Rol.objects.all()  # Consulta que obtiene todos los roles  
    serializer_class = RolSerializer  # Serializador que transforma el modelo Rol a JSON  

##########################################  
##### Clase ClasificacionViewSet #########  
##########################################  
class ClasificacionViewSet(viewsets.ModelViewSet):  
    queryset = Clasificacion.objects.all()  # Consulta que obtiene todas las clasificaciones  
    serializer_class = ClasificacionSerializer  # Serializador que transforma el modelo Clasificacion a JSON  

##################################  
##### Clase TaskViewSet ##########  
##################################  
class TaskViewSet(viewsets.ModelViewSet):  
    queryset = Task.objects.all()  # Consulta que obtiene todas las tareas  
    serializer_class = TaskSerializer  # Serializador que transforma el modelo Task a JSON