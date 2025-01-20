##############################  
##### Serializers para Tareas ## 
##############################  

from rest_framework import serializers  # Importamos el módulo serializers de Django REST Framework  
from .models import Task, Prioridad, Status, Clasificacion  # Importamos los modelos necesarios  
from usuarios.models import Usuario  # Importamos el modelo Usuario  

##################################  
##### Clase PrioridadSerializer ## 
##################################  
class PrioridadSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Prioridad  # Modelo que se va a serializar  
        fields = '__all__'  # Incluimos todos los campos del modelo  

##################################  
##### Clase StatusSerializer ##### 
##################################  
class StatusSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Status  # Modelo que se va a serializar  
        fields = '__all__'  # Incluimos todos los campos del modelo  

##########################################  
##### Clase ClasificacionSerializer ######
##########################################  
class ClasificacionSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Clasificacion  # Modelo que se va a serializar  
        fields = '__all__'  # Incluimos todos los campos del modelo  

##################################  
##### Clase TaskSerializer #######  
##################################  

class TaskSerializer(serializers.ModelSerializer):  
    area_nombre = serializers.CharField(source='area.nombre', read_only=True)  # Campo solo de lectura para el nombre del área  
    usuario_nombre = serializers.CharField(source='usuario.first_name', read_only=True)  # Campo solo de lectura para el nombre del usuario  
    status_nombre = serializers.CharField(source='status.estado', read_only=True)  # Campo solo de lectura para el estado  
    prioridad_nombre = serializers.CharField(source='prioridad.nivel', read_only=True)  # Campo solo de lectura para el nivel de prioridad  
    clasificacion_tema = serializers.CharField(source='clasificacion.tema', read_only=True)  # Campo solo de lectura para el tema de clasificación  
    tecnicos_nombres = serializers.SerializerMethodField()  # Campo personalizado para obtener los nombres de técnicos  

    class Meta:  
        model = Task  # Modelo que se va a serializar  
        fields = [  
            'id',   
            'incidencia',   
            'descripcion',   
            'area',   
            'area_nombre',   
            'usuario',   
            'usuario_nombre',   
            'tecnicos',   
            'tecnicos_nombres',  
            'status',   
            'status_nombre',   
            'prioridad',   
            'prioridad_nombre',  
            'fecha_creacion',  # Incluir fecha de creación  
            'fecha_final',  # Incluir fecha final  
            'clasificacion',  
            'clasificacion_tema'  
        ]  

    def get_tecnicos_nombres(self, obj):  
        # Método para obtener los nombres completos de los técnicos  
        return [f"{tecnico.first_name} {tecnico.last_name}" for tecnico in obj.tecnicos.all()]