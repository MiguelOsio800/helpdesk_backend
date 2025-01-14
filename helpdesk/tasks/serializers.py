# tasks/serializers.py  
from rest_framework import serializers  
from .models import Task, Prioridad, Status, Clasificacion  
from usuarios.models import Usuario  

class PrioridadSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Prioridad  
        fields = '__all__'  

class StatusSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Status  
        fields = '__all__'  

class ClasificacionSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Clasificacion  
        fields = '__all__'  

class TaskSerializer(serializers.ModelSerializer):  
    area_nombre = serializers.CharField(source='area.nombre', read_only=True)  
    usuario_nombre = serializers.CharField(source='usuario.nombres', read_only=True)  
    status_nombre = serializers.CharField(source='status.estado', read_only=True)  
    prioridad_nombre = serializers.CharField(source='prioridad.nivel', read_only=True)  
    clasificacion_tema = serializers.CharField(source='clasificacion.tema', read_only=True)  
    tecnicos_nombres = serializers.SerializerMethodField()  

    class Meta:  
        model = Task  
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
            'fecha_creacion',  # Incluir fecha_creacion  
            'fecha_final',  # Incluir fecha_final  
            'clasificacion',  
            'clasificacion_tema'  
        ]  

    def get_tecnicos_nombres(self, obj):  
        return [f"{tecnico.nombres} {tecnico.apellidos}" for tecnico in obj.tecnicos.all()]