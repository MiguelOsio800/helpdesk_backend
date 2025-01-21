from rest_framework import serializers  # Importamos el módulo serializers de Django REST Framework  
from .models import Task, Prioridad, Status, Clasificacion  # Importamos los modelos necesarios  
from usuarios.models import Usuario  # Importamos el modelo Usuario  
from .models import Informe

class InformeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Informe
        fields = ['id', 'task', 'area', 'usuario', 'equipo', 'numero_de_bien', 'motivo', 'solucion', 'status', 'observacion', 'completado']


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
    area_nombre = serializers.CharField(source='area.nombre', read_only=True)  
    usuario_nombre = serializers.CharField(source='usuario.first_name', read_only=True)  
    status_nombre = serializers.CharField(source='status.estado', read_only=True)  
    prioridad_nombre = serializers.CharField(source='prioridad.nivel', read_only=True)  
    clasificacion_tema = serializers.CharField(source='clasificacion.tema', read_only=True)  
    tecnicos_nombres = serializers.SerializerMethodField()  

    # Se añaden los campos para permisos de escritura  
    tecnicos = serializers.PrimaryKeyRelatedField(many=True, queryset=Usuario.objects.all(), required=False)  
    prioridad = serializers.PrimaryKeyRelatedField(queryset=Prioridad.objects.all(), required=False)  

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
            'fecha_creacion',  
            'fecha_final',  
            'clasificacion',  
            'clasificacion_tema'  
        ]  

    def get_tecnicos_nombres(self, obj):  
        return [f"{tecnico.first_name} {tecnico.last_name}" for tecnico in obj.tecnicos.all()]  

    def update(self, instance, validated_data):  
        # Actualizamos los técnicos  
        tecnicos = validated_data.pop('tecnicos', None)  
        if tecnicos is not None:  
            instance.tecnicos.set(tecnicos)  # Establece la relación con los nuevos técnicos  

        # Actualizar la prioridad si se proporciona  
        prioridad = validated_data.pop('prioridad', None)  
        if prioridad is not None:  
            instance.prioridad = prioridad  

        # Actualizamos los otros campos del modelo  
        for attr, value in validated_data.items():  
            setattr(instance, attr, value)  
        instance.save()  
        return instance