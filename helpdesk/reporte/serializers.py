from rest_framework import serializers
from tasks.models import Task  

class ReporteSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Task  
        fields = '__all__' 
        
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'incidencia': instance.incidencia,
            'area': instance.area.nombre,
            
        }