from django.urls import URLPattern
from rest_framework.routers import DefaultRouter

from .views import ReporteViewSet

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'reporte', ReporteViewSet, basename='reporte')


urlpatterns = router.urls