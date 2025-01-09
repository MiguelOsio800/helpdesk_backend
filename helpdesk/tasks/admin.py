from django.contrib import admin  
from .models import Task  # Importamos solo Task  

class TaskAdmin(admin.ModelAdmin):  
    list_display = ('incidencia', 'area', 'usuario', 'status', 'prioridad')  # Muestra estos campos, incluyendo 'prioridad'  
    list_filter = ('area', 'status', 'prioridad')  # Permitir filtrar por área, estado y prioridad  
    search_fields = ('incidencia', 'descripcion')  
    filter_horizontal = ('tecnicos',)  # Mejora la selección de múltiples técnicos  

# Registra solo el modelo Task con su administrador  
admin.site.register(Task, TaskAdmin)