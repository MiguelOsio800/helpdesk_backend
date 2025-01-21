from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, PrioridadViewSet, StatusViewSet, ClasificacionViewSet, InformeViewSet  # Importar el nuevo viewset

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'prioridades', PrioridadViewSet)
router.register(r'status', StatusViewSet)
router.register(r'clasificaciones', ClasificacionViewSet)
router.register(r'informes', InformeViewSet)  # Registrar el ViewSet para Informes

urlpatterns = [
    path('', include(router.urls)),
]
