# tasks/urls.py  
from django.urls import path, include  
from rest_framework.routers import DefaultRouter  
from .views import TaskViewSet, PrioridadViewSet, StatusViewSet, ClasificacionViewSet  # Elimina NumeroBienViewSet  

router = DefaultRouter()  
router.register(r'tasks', TaskViewSet)  
router.register(r'prioridades', PrioridadViewSet)  
router.register(r'status', StatusViewSet)  
router.register(r'clasificaciones', ClasificacionViewSet)  

urlpatterns = [  
    path('', include(router.urls)),  
]