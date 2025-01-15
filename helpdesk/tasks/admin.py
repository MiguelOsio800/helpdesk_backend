# tasks/admin.py  
from django.contrib import admin  
from .models import Task, Prioridad, Status, Clasificacion  # Asegúrate de que NumeroBien no esté aquí  

class TaskAdmin(admin.ModelAdmin):  
    # (código para TaskAdmin)  
    ...  

class PrioridadAdmin(admin.ModelAdmin):  
    # (código para PrioridadAdmin)  
    ...  

class StatusAdmin(admin.ModelAdmin):  
    # (código para StatusAdmin)  
    ...  

class ClasificacionAdmin(admin.ModelAdmin):  
    # (código para ClasificacionAdmin)  
    ...  

# Registro de los modelos en el admin  
admin.site.register(Task, TaskAdmin)  
admin.site.register(Prioridad, PrioridadAdmin)  
admin.site.register(Status, StatusAdmin)  
admin.site.register(Clasificacion, ClasificacionAdmin)