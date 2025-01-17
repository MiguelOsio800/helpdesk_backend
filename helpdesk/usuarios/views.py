from rest_framework import viewsets  
from rest_framework.response import Response  
from .models import Usuario, Area, Rol, Clasificacion, Task  
from .serializers import UsuarioSerializer, AreaSerializer, RolSerializer, ClasificacionSerializer, TaskSerializer  

class UsuarioViewSet(viewsets.ModelViewSet):  
    queryset = Usuario.objects.all()  
    serializer_class = UsuarioSerializer  

    def list(self, request, *args, **kwargs):  
        return super().list(request, *args, **kwargs)  # Esto devolverá todos los usuarios  

    def list_tecnicos(self, request, *args, **kwargs):  
        # Filtramos los usuarios que tienen rol técnico  
        rol_tecnico = Rol.objects.filter(nombre='tecnico').first()  # Asegúrate de que 'tecnico' es el nombre correcto del rol.  
        if rol_tecnico:  
            usuarios_tecnicos = self.queryset.filter(rol=rol_tecnico)  
            serializer = self.get_serializer(usuarios_tecnicos, many=True)  
            return Response(serializer.data)  
        return Response([])  # Devuelve una lista vacía si no hay técnicos  
    
    def list_tecnologia(self, request, *args, **kwargs):  
        # Filtramos los usuarios que tienen el area tecnología  
        area_tecnologia = Area.objects.filter(nombre='Tecnologia').first()  # Asegúrate de que 'tecnico' es el nombre correcto del rol.  
        if area_tecnologia:  
            usuarios_tecnologia = self.queryset.filter(area=area_tecnologia)  
            serializer = self.get_serializer(usuarios_tecnologia, many=True)  
            return Response(serializer.data)  
        return Response([])  # Devuelve una lista vacía si no hay técnicos  
  
class AreaViewSet(viewsets.ModelViewSet):  
    queryset = Area.objects.all()  
    serializer_class = AreaSerializer  

class RolViewSet(viewsets.ModelViewSet):  
    queryset = Rol.objects.all()  
    serializer_class = RolSerializer  

class ClasificacionViewSet(viewsets.ModelViewSet):  
    queryset = Clasificacion.objects.all()  
    serializer_class = ClasificacionSerializer  

class TaskViewSet(viewsets.ModelViewSet):  
    queryset = Task.objects.all()  
    serializer_class = TaskSerializer