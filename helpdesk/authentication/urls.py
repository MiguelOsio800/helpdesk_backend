# authentication/urls.py  

from django.urls import path  
from .views import LoginView  
from rest_framework_simplejwt.views import TokenRefreshView  # Si estás usando refresh tokens  

urlpatterns = [  
    path('api/auth/login/', LoginView.as_view(), name='login'),  # Ruta para el inicio de sesión  
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Ruta para refrescar el token  
]