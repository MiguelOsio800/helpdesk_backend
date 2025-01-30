from rest_framework import serializers  
from .models import Task, Prioridad, Status, Clasificacion  
from usuarios.models import Usuario  # Asegúrate de que esta línea apunte a la ubicación correcta  
from informes.models import Informe

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
    area_nombre = serializers.CharField(source='area.nombre', read_only=True)  # Solo para la representación  
    usuario_nombre = serializers.CharField(source='usuario.first_name', read_only=True)  
    status_nombre = serializers.CharField(source='status.estado', read_only=True)  
    prioridad_nombre = serializers.CharField(source='prioridad.nivel', read_only=True)  
    clasificacion_tema = serializers.CharField(source='clasificacion.clasificacion', read_only=True)  
    
    tecnicos = serializers.PrimaryKeyRelatedField(many=True, queryset=Usuario.objects.all(), required=False)  
    prioridad = serializers.PrimaryKeyRelatedField(queryset=Prioridad.objects.all(), required=False)  

    def to_representation(self, tarea):
       return {
           'id': tarea.id,
           'incidencia': tarea.incidencia,
           'descripcion': tarea.descripcion,
           'area': tarea.area.id,
           'area_nombre': tarea.area.nombre,
           'usuario': tarea.usuario.id,
           'usuario_nombre': tarea.usuario.first_name,
           'tecnicos': [tecnico.id for tecnico in tarea.tecnicos.all()],
           'status': tarea.status.id,
           'status_nombre': tarea.status.estado,
           'prioridad': tarea.prioridad.id if tarea.prioridad != None else None,
           'prioridad_nombre': tarea.prioridad.nivel if tarea.prioridad != None else 'Sin prioridad',
           'fecha_creacion': tarea.fecha_creacion,
           'fecha_final': tarea.fecha_final,
           'clasificacion': tarea.clasificacion.id if tarea.clasificacion != None else None,
           'clasificacion_tema': tarea.clasificacion.clasificacion if tarea.clasificacion != None else 'Sin clasificación',
           'reportes': [
               {
                   'id': informe.id,
                   'area': informe.area.id,
                   'usuario': informe.usuario.id,
                   'usuario_nombre': informe.usuario.first_name,
                   'usuario_apellido': informe.usuario.last_name,
                   'equipo': informe.equipo,
                   'numero_de_bien': informe.numero_de_bien,
                   'solucion': informe.solucion,
                   'observacion': informe.observacion,
                   'completado': informe.completado
               } for informe in Informe.objects.filter(task=tarea)
           ]
       }
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
            'status',  
            'status_nombre',  
            'prioridad',  
            'prioridad_nombre',  
            'fecha_creacion',  
            'fecha_final',  
            'clasificacion',  
            'clasificacion_tema',  
        ]  

    def update(self, instance, validated_data):  
        tecnicos = validated_data.pop('tecnicos', None)  
        if tecnicos is not None:  
            instance.tecnicos.set(tecnicos)  

        prioridad = validated_data.pop('prioridad', None)  
        if prioridad is not None:  
            instance.prioridad = prioridad  

        for attr, value in validated_data.items():  
            setattr(instance, attr, value)  
        instance.save()  
        return instance