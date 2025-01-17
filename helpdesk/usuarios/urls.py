from django.urls import path, include  
from rest_framework.routers import DefaultRouter  
from .views import UsuarioViewSet, AreaViewSet, RolViewSet, ClasificacionViewSet, TaskViewSet  

router = DefaultRouter()  
router.register(r'usuarios', UsuarioViewSet)  
router.register(r'areas', AreaViewSet)  
router.register(r'roles', RolViewSet)  
router.register(r'clasificaciones', ClasificacionViewSet)  
router.register(r'tareas', TaskViewSet)  

urlpatterns = [  
    path('', include(router.urls)),  
    path('tecnicos/', UsuarioViewSet.as_view({'get': 'list_tecnicos'}), name='usuarios-tecnicos'),
    path('tecnologia/', UsuarioViewSet.as_view({'get': 'list_tecnologia'}), name='usuarios-tecnicos'),
]  