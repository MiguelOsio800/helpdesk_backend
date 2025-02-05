from django.urls import path, include  
from rest_framework.routers import DefaultRouter  
from .views import UsuarioViewSet, AreaViewSet, RolViewSet, ClasificacionViewSet, TaskViewSet  

# Configuración del router  
router = DefaultRouter()  
router.register(r'usuarios', UsuarioViewSet)  
router.register(r'areas', AreaViewSet)  
router.register(r'roles', RolViewSet)  
router.register(r'clasificaciones', ClasificacionViewSet)  
router.register(r'tareas', TaskViewSet)  

# Definición de las URLs  
urlpatterns = [  
    path('', include(router.urls)),  
]