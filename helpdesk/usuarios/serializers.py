from rest_framework import serializers  
from .models import Usuario, Area, Rol, Clasificacion, Task  

# Serializador para el modelo Area  
class AreaSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Area  
        fields = ['id', 'nombre']  # Especifica los campos que realmente quieras mostrar  

# Serializador para el modelo Rol  
class RolSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Rol  
        fields = ['id', 'nombre']  # Especifica los campos que realmente quieras mostrar  

# Serializador para el modelo Usuario  
class UsuarioSerializer(serializers.ModelSerializer):  
    rol_nombre = serializers.CharField(source='rol.nombre', read_only=True)

    class Meta:  
        model = Usuario  
        fields = ['id', 'username', 'first_name', 'last_name', 'email','rol', 'rol_nombre']  # Solo incluye los campos que solicitaste  

# Serializador para el modelo Clasificacion  
class ClasificacionSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Clasificacion  
        fields = ['id', 'nombre']  # Especifica los campos que realmente quieras mostrar  

# Serializador para el modelo Task  
class TaskSerializer(serializers.ModelSerializer):  
    clasificacion_data = ClasificacionSerializer(source="clasificacion", read_only=True)  
    usuario_asignado_data = UsuarioSerializer(source="usuario_asignado", read_only=True)  

    class Meta:  
        model = Task  
        fields = ['id', 'titulo', 'clasificacion_data', 'usuario_asignado_data']  # Especifica los campos necesarios