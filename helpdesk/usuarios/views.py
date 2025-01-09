# views.py  
from rest_framework import viewsets  
from .models import Usuario, Area, Rol  
from .serializers import UsuarioSerializer, AreaSerializer, RolSerializer  

class UsuarioViewSet(viewsets.ModelViewSet):  
    queryset = Usuario.objects.all()  
    serializer_class = UsuarioSerializer  

class AreaViewSet(viewsets.ModelViewSet):  
    queryset = Area.objects.all()  
    serializer_class = AreaSerializer  

class RolViewSet(viewsets.ModelViewSet):  
    queryset = Rol.objects.all()  
    serializer_class = RolSerializer