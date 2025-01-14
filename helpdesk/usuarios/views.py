from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Usuario, Area, Rol
from .serializers import UsuarioSerializer, AreaSerializer, RolSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    # Agregamos una acción personalizada para filtrar usuarios por rol
    @action(detail=False, methods=['get'], url_path='tecnicos')
    def tecnicos(self, request):
        # Filtrar usuarios cuyo rol sea "técnico"
        rol_tecnico = Rol.objects.filter(nombre__iexact='tecnico').first()
        if rol_tecnico:
            usuarios_tecnicos = Usuario.objects.filter(rol=rol_tecnico)
            serializer = self.get_serializer(usuarios_tecnicos, many=True)
            return Response(serializer.data)
        return Response([], status=200)

class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
