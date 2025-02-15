"""  
Django settings for helpdesk project.  

Generated by 'django-admin startproject' using Django 5.1.4.  

For more information on this file, see  
https://docs.djangoproject.com/en/5.1/topics/settings/  

For the full list of settings and their values, see  
https://docs.djangoproject.com/en/5.1/ref/settings/  
"""  

from pathlib import Path  
from datetime import timedelta  # Importar timedelta para la configuración de JWT  

# Build paths inside the project like this: BASE_DIR / 'subdir'.  
BASE_DIR = Path(__file__).resolve().parent.parent  

# Quick-start development settings - unsuitable for production  
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/  

# SECURITY WARNING: keep the secret key used in production secret!  
SECRET_KEY = 'django-insecure-9-u5j5)sj5uf&$ft2-)7cfvw$#fpcl21+x6ru2u_l7)aj&6^_s'  

# SECURITY WARNING: don't run with debug turned on in production!  
DEBUG = True  

ALLOWED_HOSTS = []  

# Application definition  

INSTALLED_APPS = [  
    'django.contrib.admin',  
    'django.contrib.auth',  
    'django.contrib.contenttypes',  
    'django.contrib.sessions',  
    'django.contrib.messages',  
    'django.contrib.staticfiles',  
    'rest_framework',  
    'usuarios',  
    'tasks',  
    'informes.apps.InformesConfig',
    'authentication',   
    'rest_framework_simplejwt',  
    'corsheaders',  
    'django_extensions',  
]

MIDDLEWARE = [  
    'django.middleware.security.SecurityMiddleware',  
    'django.contrib.sessions.middleware.SessionMiddleware',  
    'django.middleware.common.CommonMiddleware',  
    'django.middleware.csrf.CsrfViewMiddleware',  
    'django.contrib.auth.middleware.AuthenticationMiddleware',  
    'django.contrib.messages.middleware.MessageMiddleware',  
    'django.middleware.clickjacking.XFrameOptionsMiddleware', 
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware', 
]  

# Permitir el origen de Angular
CORS_ALLOWED_ORIGINS = [
    "http://localhost:4200",  # URL del frontend en desarrollo
]

ROOT_URLCONF = 'helpdesk.urls'  

TEMPLATES = [  
    {  
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  
        'DIRS': [],  
        'APP_DIRS': True,  
        'OPTIONS': {  
            'context_processors': [  
                'django.template.context_processors.debug',  
                'django.template.context_processors.request',  
                'django.contrib.auth.context_processors.auth',  
                'django.contrib.messages.context_processors.messages',  
            ],  
        },  
    },  
]  

WSGI_APPLICATION = 'helpdesk.wsgi.application'  

# Database  
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases  

DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.postgresql',  
        'NAME': 'helpdesk_db',  # Nombre de la base de datos que acabas de crear  
        'USER': 'postgres',      # Usuario de postgres (o el que hayas creado)  
        'PASSWORD': '123',  # Contraseña de postgres (o la que hayas creado)  
        'HOST': 'localhost',  
        'PORT': '5432',  
    }  
}  

# Password validation  
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators  

AUTH_PASSWORD_VALIDATORS = [  
    {  
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  
    },  
    {  
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  
    },  
    {  
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  
    },  
    {  
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  
    },  
]  

# Internationalization  
# https://docs.djangoproject.com/en/5.1/topics/i18n/  

LANGUAGE_CODE = 'en-us'  

TIME_ZONE = 'America/Caracas' 

USE_I18N = True  

USE_TZ = True  

# Static files (CSS, JavaScript, Images)  
# https://docs.djangoproject.com/en/5.1/howto/static-files/  

STATIC_URL = 'static/'  

# Default primary key field type  
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field  

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  

# Configuración de Django REST Framework  
REST_FRAMEWORK = {  
    'DEFAULT_AUTHENTICATION_CLASSES': (  
        'rest_framework_simplejwt.authentication.JWTAuthentication',  
    ),  
}  

# Configuración de Simple JWT  
SIMPLE_JWT = {  
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=8),  # Tiempo de vida del token de acceso  
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),     # Tiempo de vida del token de actualización  
    'ROTATE_REFRESH_TOKENS': True,                    # Rotar tokens de actualización  
    'BLACKLIST_AFTER_USE': True,                       # Agregar a la lista negra después de su uso  
}

AUTH_USER_MODEL = "usuarios.Usuario"