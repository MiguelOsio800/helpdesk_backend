# serializers.py  
from rest_framework import serializers  
from .models import Informe  

class InformeSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Informe  
        fields = '__all__'  # O especifica los campos que necesitas