from django.urls import path, include  
from rest_framework.routers import DefaultRouter  
from .views import TaskViewSet  # Asegúrate de que solo importes TaskViewSet  

router = DefaultRouter()  
router.register(r'tasks', TaskViewSet)  

urlpatterns = [  
    path('', include(router.urls)),  
]  