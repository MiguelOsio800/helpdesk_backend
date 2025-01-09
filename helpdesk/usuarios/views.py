from rest_framework import viewsets  
from .models import Usuario, Area  
from .serializers import UsuarioSerializer, AreaSerializer  

class UsuarioViewSet(viewsets.ModelViewSet):  
    queryset = Usuario.objects.all()  
    serializer_class = UsuarioSerializer  

class AreaViewSet(viewsets.ModelViewSet):  
    queryset = Area.objects.all()  
    serializer_class = AreaSerializer