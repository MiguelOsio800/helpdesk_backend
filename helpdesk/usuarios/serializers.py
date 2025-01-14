from rest_framework import serializers  
from .models import Usuario, Area, Rol  

class AreaSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Area  
        fields = '__all__'  

class RolSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Rol  
        fields = '__all__'  

class UsuarioSerializer(serializers.ModelSerializer):  
    areadata = AreaSerializer(source="area", read_only=True)  
    roldata = RolSerializer(source="rol", read_only=True)  

    class Meta:  
        model = Usuario  
        fields = '__all__' 