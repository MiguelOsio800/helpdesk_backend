# tasks/urls.py  
from django.urls import path, include  
from rest_framework.routers import DefaultRouter  
from .views import TaskViewSet, PrioridadViewSet  

router = DefaultRouter()  
router.register(r'tasks', TaskViewSet)  
router.register(r'prioridades', PrioridadViewSet)  # Registro del EndPoint para Prioridades  

urlpatterns = [  
    path('', include(router.urls)),  
]