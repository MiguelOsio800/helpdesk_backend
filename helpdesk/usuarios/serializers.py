####################################################  
##### Serializadores para el Sistema de Tareas #####  
####################################################  

from rest_framework import serializers  # Importamos el módulo serializers de Django REST Framework  
from .models import Usuario, Area, Rol, Clasificacion, Task  # Importamos los modelos necesarios  

##################################  
##### Clase AreaSerializer #######
##################################  
class AreaSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Area  # Modelo que se va a serializar  
        fields = ['id', 'nombre']  # Especifica los campos que realmente quieres mostrar  

##################################  
##### Clase RolSerializer ######## 
##################################  
class RolSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Rol  # Modelo que se va a serializar  
        fields = ['id', 'nombre']  # Especifica los campos que realmente quieres mostrar  

##################################  
##### Clase UsuarioSerializer ####  
##################################  
class UsuarioSerializer(serializers.ModelSerializer):  
    rol_nombre = serializers.CharField(source='rol.nombre', read_only=True)  # Campo solo de lectura para el nombre del rol asociado  

    class Meta:  
        model = Usuario  # Modelo que se va a serializar  
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'rol', 'rol_nombre','password','area']  # Solo incluye los campos que solicitaste  

##########################################  
##### Clase ClasificacionSerializer ######  
##########################################  
class ClasificacionSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Clasificacion  # Modelo que se va a serializar  
        fields = ['id', 'nombre']  # Especifica los campos que realmente quieras mostrar  

##################################  
##### Clase TaskSerializer ####### 
##################################  
class TaskSerializer(serializers.ModelSerializer):  
    clasificacion_data = ClasificacionSerializer(source="clasificacion", read_only=True)  # Serializador anidado para clasificaciones  
    usuario_asignado_data = UsuarioSerializer(source="usuario", read_only=True)  # Serializador anidado para usuarios asignados  

    class Meta:  
        model = Task  # Modelo que se va a serializar  
        fields = ['id', 'titulo', 'clasificacion_data', 'usuario_asignado_data']  # Especifica los campos necesarios