# tasks/urls.py  
from django.urls import path, include  
from rest_framework.routers import DefaultRouter  
from .views import TaskViewSet, PrioridadViewSet, StatusViewSet, ClasificacionViewSet  # Importar el nuevo viewset  

router = DefaultRouter()  
router.register(r'tasks', TaskViewSet)  
router.register(r'prioridades', PrioridadViewSet)  
router.register(r'status', StatusViewSet)  # Registro del EndPoint para Status  
router.register(r'clasificaciones', ClasificacionViewSet)  # Registro del EndPoint para Clasificaciones  

urlpatterns = [  
    path('', include(router.urls)),  
]