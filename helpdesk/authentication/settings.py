# settings.py  

from datetime import timedelta  

SIMPLE_JWT = {  
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),  # Token de acceso expira en 30 minutos  
    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=30),  # Token de refresco expira en 30 minutos  
    'ROTATE_REFRESH_TOKENS': True,  
}