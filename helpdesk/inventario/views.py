# inventario/views.py  
from rest_framework import viewsets  
from .models import Equipo, TipoEquipo, NumeroBien  
from .serializers import EquipoSerializer, TipoEquipoSerializer, NumeroBienSerializer  
from rest_framework.permissions import IsAuthenticated  

class TipoEquipoViewSet(viewsets.ModelViewSet):  
    queryset = TipoEquipo.objects.all()  
    serializer_class = TipoEquipoSerializer  
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder  

class NumeroBienViewSet(viewsets.ModelViewSet):  
    queryset = NumeroBien.objects.all()  
    serializer_class = NumeroBienSerializer  
    permission_classes = [IsAuthenticated]  

class EquipoViewSet(viewsets.ModelViewSet):  
    queryset = Equipo.objects.all()  
    serializer_class = EquipoSerializer  
    permission_classes = [IsAuthenticated]