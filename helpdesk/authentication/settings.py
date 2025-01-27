# settings.py  

from datetime import timedelta  

SIMPLE_JWT = {  
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=8),  # Token de acceso expira en 8 horas  
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),  # Token de refresco expira en 1 día (puedes ajustarlo según tus necesidades)  
    'ROTATE_REFRESH_TOKENS': True,  
}  