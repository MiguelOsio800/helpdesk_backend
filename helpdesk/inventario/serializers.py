# inventario/serializers.py  
from rest_framework import serializers  
from .models import Equipo, TipoEquipo, NumeroBien  

class TipoEquipoSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = TipoEquipo  
        fields = '__all__'  

class NumeroBienSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = NumeroBien  
        fields = '__all__'  

class EquipoSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Equipo  
        fields = '__all__'