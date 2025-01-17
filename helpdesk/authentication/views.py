#####################################  
##### Vista de Inicio de Sesión #####  
#####################################  

from django.shortcuts import render  # Importamos render para renderizar plantillas (no utilizado aquí pero comúnmente importado)  
from rest_framework_simplejwt.tokens import RefreshToken  # Importamos RefreshToken para manejar tokens JWT  
from rest_framework.response import Response  # Importamos Response para devolver respuestas HTTP  
from rest_framework.views import APIView  # Importamos APIView para crear vistas basadas en clases  
from django.contrib.auth import authenticate  # Importamos authenticate para validar las credenciales del usuario  
from rest_framework import status  # Importamos status para gestionar estados HTTP  

#####################################
##### Clase LoginView ###############  
#####################################
class LoginView(APIView):  
    def post(self, request):  
        username = request.data.get('username')  # Obtiene el nombre de usuario del cuerpo de la solicitud  
        password = request.data.get('password')  # Obtiene la contraseña del cuerpo de la solicitud  

        # Verificar que se ha proporcionado username y password  
        if not username or not password:  
            return Response({'error': 'El usuario y contraseña son requeridos.'}, status=status.HTTP_400_BAD_REQUEST)  # Respuesta de error si faltan credenciales  

        user = authenticate(request, username=username, password=password)  # Autenticación del usuario mediante las credenciales  

        if user is not None:  # Si el usuario fue encontrado  
            refresh = RefreshToken.for_user(user)  # Genera un refresh token para el usuario autenticado  
            access_token = refresh.access_token  # Obtiene el access token del refresh token  
            access_token["user_data"] = {  # Agrega datos adicionales al access token  
                "id": user.id,  
                "username": user.username,  
                "nombres": user.first_name,  
                "apellidos": user.last_name,  
                "email": user.email,  
                "rol": user.rol.nombre if user.rol else None,  
                "area": user.area.nombre if user.area else None,  
            }  
            return Response({  
                'access_token': str(access_token),  # Devuelve el access token como cadena  
                'refresh_token': str(refresh)  # Devuelve el refresh token como cadena  
            })  
        else:  # Credenciales inválidas  
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)  # Respuesta de error para credenciales inválidas