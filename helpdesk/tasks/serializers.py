from rest_framework import serializers  
from .models import Task, Prioridad, Status, Clasificacion, Usuario  # Asegúrate de importar Usuario  

class PrioridadSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Prioridad  # Cambiado de string a referencia del modelo  
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
    usuario_nombre = serializers.CharField(source='usuario.first_name', read_only=True)  
    status_nombre = serializers.CharField(source='status.estado', read_only=True)  
    prioridad_nombre = serializers.CharField(source='prioridad.nivel', read_only=True)  # Verifica si el campo 'nivel' existe en Prioridad  
    clasificacion_tema = serializers.CharField(source='clasificacion.clasificacion', read_only=True)  
    tecnicos_nombres = serializers.SerializerMethodField()  

    # Aquí corrige el queryset  
    tecnicos = serializers.PrimaryKeyRelatedField(many=True, queryset=Usuario.objects.all(), required=False)  # Cambiado de string a queryset real  
    prioridad = serializers.PrimaryKeyRelatedField(queryset=Prioridad.objects.all(), required=False)  

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
            'fecha_creacion',  
            'fecha_final',  
            'clasificacion',  
            'clasificacion_tema'  
        ]  

    def get_tecnicos_nombres(self, obj):  
        return [f"{tecnico.first_name} {tecnico.last_name}" for tecnico in obj.tecnicos.all()]  

    def update(self, instance, validated_data):  
        tecnicos = validated_data.pop('tecnicos', None)  
        if tecnicos is not None:  
            instance.tecnicos.set(tecnicos)  

        prioridad = validated_data.pop('prioridad', None)  
        if prioridad is not None:  
            instance.prioridad = prioridad  # Asegúrate de que prioridad sea un objeto válido  

        for attr, value in validated_data.items():  
            setattr(instance, attr, value)  
        instance.save()  
        return instance