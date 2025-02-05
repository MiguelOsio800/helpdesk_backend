from rest_framework import viewsets  
from rest_framework.response import Response  
from rest_framework.decorators import action  # Importar el decorador @action  
from .models import Usuario, Area, Rol, Clasificacion, Task  
from .serializers import UsuarioSerializer, AreaSerializer, RolSerializer, ClasificacionSerializer, TaskSerializer  

##################################  
##### Clase UsuarioViewSet #######  
##################################  
class UsuarioViewSet(viewsets.ModelViewSet):  
    queryset = Usuario.objects.all()  
    serializer_class = UsuarioSerializer  

    def list(self, request, *args, **kwargs):  
        return super().list(request, *args, **kwargs)  

    @action(detail=False, methods=['get'], url_path='tecnicos')  # Método para listar técnicos  
    def list_tecnicos(self, request, *args, **kwargs):  
        try:  
            rol_tecnico = Rol.objects.get(nombre='Tecnico')  # Buscar rol 'Tecnico'  
        except Rol.DoesNotExist:  
            print("No se encontró el rol 'Tecnico'.")  
            return Response([], status=404)  # Retornar 404 si no se encuentra el rol  

        usuarios_tecnicos = self.queryset.filter(rol=rol_tecnico)  # Filtrar usuarios con rol técnico  
        print(f"Usuarios técnicos encontrados: {usuarios_tecnicos.count()}")  
        serializer = self.get_serializer(usuarios_tecnicos, many=True)  
        return Response(serializer.data)  
    
    @action(detail=False, methods=['get'], url_path='tecnologia')  # Método para listar tecnología  
    def list_tecnologia(self, request, *args, **kwargs):  
        area_tecnologia = Area.objects.filter(nombre='Tecnologia').first()  
        if area_tecnologia:  
            usuarios_tecnologia = self.queryset.filter(area=area_tecnologia)  
            serializer = self.get_serializer(usuarios_tecnologia, many=True)  
            return Response(serializer.data)  
        print("No se encontró el área 'Tecnologia'.")  
        return Response([])  

    def create(self, request, *args, **kwargs):  
        print("Creando Usuario")  
        serializer = self.get_serializer(data=request.data)  
        serializer.is_valid(raise_exception=True)  
        usuario = serializer.save()  

        if 'password' in request.data:  
            usuario.set_password(request.data['password'])  
            usuario.save()  

        return Response(serializer.data)  

##################################  
##### Clase AreaViewSet ##########  
##################################  
class AreaViewSet(viewsets.ModelViewSet):  
    queryset = Area.objects.all()  
    serializer_class = AreaSerializer  

##################################  
##### Clase RolViewSet ###########  
##################################  
class RolViewSet(viewsets.ModelViewSet):  
    queryset = Rol.objects.all()  
    serializer_class = RolSerializer  

##########################################  
##### Clase ClasificacionViewSet #########  
##########################################  
class ClasificacionViewSet(viewsets.ModelViewSet):  
    queryset = Clasificacion.objects.all()  
    serializer_class = ClasificacionSerializer  

##################################  
##### Clase TaskViewSet ##########  
##################################  
class TaskViewSet(viewsets.ModelViewSet):  
    queryset = Task.objects.all()  
    serializer_class = TaskSerializer