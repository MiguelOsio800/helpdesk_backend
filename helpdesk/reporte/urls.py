from django.urls import path  
from .views import completar_informe, ReporteViewSet  
from rest_framework.routers import DefaultRouter  

router = DefaultRouter()  
router.register('informes', ReporteViewSet)  

urlpatterns = [  
    path('completar-informe/<int:task_id>/', completar_informe, name='completar_informe'),  
] + router.urls