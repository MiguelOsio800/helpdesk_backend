from django.urls import path, include  
from rest_framework.routers import DefaultRouter  
from .views import UsuarioViewSet, AreaViewSet, RolViewSet  # Asegúrate de que RolViewSet esté importado  

router = DefaultRouter()  
router.register(r'usuarios', UsuarioViewSet)  
router.register(r'areas', AreaViewSet)  # Añadir rutas para Area  
router.register(r'roles', RolViewSet)  # Añadir rutas para Rol  

urlpatterns = [  
    path('', include(router.urls)),  
]