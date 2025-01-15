# autenticacion/views.py  
from django.shortcuts import render  
from rest_framework_simplejwt.tokens import RefreshToken  
from rest_framework.response import Response  
from rest_framework.views import APIView  
from django.contrib.auth import authenticate  
from rest_framework import status  # Importa status para gestionar estados HTTP  

# ================================  
#         VISTA: LOGIN  
# ================================  

class LoginView(APIView):  
    """Vista para manejar el inicio de sesión de los usuarios."""  
    
    def post(self, request):  
        """Gestiona las solicitudes POST para iniciar sesión.  

        Args:  
            request: Objeto de solicitud que contiene los datos del usuario.  

        Returns:  
            Response: Respuesta con tokens de acceso y actualización o un mensaje de error.  
        """  
        username = request.data.get('username')  # Obtener el nombre de usuario  
        password = request.data.get('password')  # Obtener la contraseña  

        # Verificar que se han proporcionado el nombre de usuario y la contraseña  
        if not username or not password:  
            return Response(  
                {'error': 'El usuario y contraseña son requeridos.'},  
                status=status.HTTP_400_BAD_REQUEST  
            )  

        user = authenticate(request, username=username, password=password)  # Autenticar al usuario  

        if user is not None:  # Usuario encontrado  
            refresh = RefreshToken.for_user(user)  # Crear token de actualización  
            access_token = refresh.access_token  # Crear token de acceso  

            # Añadir datos del usuario al token de acceso  
            access_token["user_data"] = {  
                "id": user.id,  
                "username": user.username,  
                "nombres": user.first_name,  
                "apellidos": user.last_name,  
                "email": user.email,  
                "rol": user.rol.nombre if user.rol else None,  
                "area": user.area.nombre if user.area else None,  
            }  
            return Response({  
                'access_token': str(access_token),  # Token de acceso  
                'refresh_token': str(refresh)  # Token de actualización  
            })  
        else:  # Credenciales inválidas  
            return Response(  
                {'error': 'Credenciales inválidas'},  
                status=status.HTTP_401_UNAUTHORIZED  
            )