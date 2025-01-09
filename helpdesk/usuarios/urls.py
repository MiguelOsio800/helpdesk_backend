from django.urls import path, include  
from rest_framework.routers import DefaultRouter  
from .views import UsuarioViewSet, AreaViewSet  

router = DefaultRouter()  
router.register(r'usuarios', UsuarioViewSet)  
router.register(r'areas', AreaViewSet)  # Añadir rutas para Area  

urlpatterns = [  
    path('', include(router.urls)),  
]