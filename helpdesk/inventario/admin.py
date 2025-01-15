# inventario/models.py  
from django.db import models  
from .models import TipoEquipo, NumeroBien, Equipo  
from tasks.models import Clasificacion  # Importa Clasificacion desde la app de tasks  
from django.contrib import admin  

# Registro de modelos en el panel de administración  
admin.site.register(TipoEquipo)   # Registrar el modelo tipo Equipo
admin.site.register(Equipo)  # Registrar el modelo Equipo
admin.site.register(NumeroBien)  # Registrar el modelo NumeroBien