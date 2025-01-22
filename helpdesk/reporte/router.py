# router.py  
from django.urls import path, include  
from rest_framework.routers import DefaultRouter  
from .views import ReporteViewSet  # Asegúrate que esto exista  

router = DefaultRouter()  
router.register(r'reportes', ReporteViewSet, basename='reporte')  # Registro del ViewSet de Reporte  

urlpatterns = [  
    path('', include(router.urls)),  
]