# inventario/urls.py  
from django.urls import path, include  
from rest_framework.routers import DefaultRouter  
from .views import EquipoViewSet, TipoEquipoViewSet, NumeroBienViewSet  

# Crear un enrutador simple para las vistas  
router = DefaultRouter()  
router.register(r'equipos', EquipoViewSet)  # Ruta para el modelo Equipo  
router.register(r'tipos_equipo', TipoEquipoViewSet)  # Ruta para el modelo TipoEquipo  
router.register(r'numeros_bien', NumeroBienViewSet)  # Ruta para el modelo NumeroBien  

# Definir las URL patterns  
urlpatterns = [  
    path('', include(router.urls)),  # Incluir las rutas de los viewsets  
]