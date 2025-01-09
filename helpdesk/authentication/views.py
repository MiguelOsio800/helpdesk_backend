from django.shortcuts import render  
from rest_framework_simplejwt.tokens import RefreshToken  
from rest_framework.response import Response  
from rest_framework.views import APIView  
from django.contrib.auth import authenticate  
from rest_framework import status  # Importar status para gestionar estados HTTP  

class LoginView(APIView):  
    def post(self, request):  
        username = request.data.get('username')  # Cambiado a username  
        password = request.data.get('password')  

        # Verificar que se ha proporcionado username y password  
        if not username or not password:  
            return Response({'error': 'El usuario y contraseña son requeridos.'}, status=status.HTTP_400_BAD_REQUEST)  

        user = authenticate(request, username=username, password=password)  

        if user is not None:  # Usuario encontrado  
            refresh = RefreshToken.for_user(user)  
            access_token = str(refresh.access_token)  
            return Response({  
                'access_token': access_token,  
                'refresh_token': str(refresh)  # Devolver también el refresh token  
            })  
        else:  # Credenciales inválidas  
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)