from rest_framework import viewsets  
from rest_framework.response import Response  
from .models import Usuario, Area, Rol, Clasificacion, Task  
from .serializers import UsuarioSerializer, AreaSerializer, RolSerializer, ClasificacionSerializer, TaskSerializer  

class UsuarioViewSet(viewsets.ModelViewSet):  
    queryset = Usuario.objects.all()  
    serializer_class = UsuarioSerializer  

    def list(self, request, *args, **kwargs):  
        # Aquí puedes personalizar la query y filtrado si lo necesitas  
        return super().list(request, *args, **kwargs) # Esto devolverá todos los usuarios con el nuevo serializer.  
  
class AreaViewSet(viewsets.ModelViewSet):  
    queryset = Area.objects.all()  
    serializer_class = AreaSerializer  

class RolViewSet(viewsets.ModelViewSet):  
    queryset = Rol.objects.all()  
    serializer_class = RolSerializer  

# Nuevo ViewSet para Clasificaciones  
class ClasificacionViewSet(viewsets.ModelViewSet):  
    queryset = Clasificacion.objects.all()  
    serializer_class = ClasificacionSerializer  

# Nuevo ViewSet para Tareas  
class TaskViewSet(viewsets.ModelViewSet):  
    queryset = Task.objects.all()  
    serializer_class = TaskSerializer