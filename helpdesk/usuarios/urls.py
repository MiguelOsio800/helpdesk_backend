from django.urls import path, include  
from rest_framework.routers import DefaultRouter  
from .views import UsuarioViewSet, AreaViewSet, RolViewSet, ClasificacionViewSet, TaskViewSet  

router = DefaultRouter()  
router.register(r'usuarios', UsuarioViewSet)  
router.register(r'areas', AreaViewSet)  
router.register(r'roles', RolViewSet)  
router.register(r'clasificaciones', ClasificacionViewSet)  # Nueva ruta para Clasificaciones  
router.register(r'tareas', TaskViewSet)  # Nueva ruta para Tareas  

urlpatterns = [  
    path('', include(router.urls)),  
]