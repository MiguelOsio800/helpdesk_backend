# tasks/admin.py  
from django.contrib import admin  
from .models import Task, Prioridad, Status 

class TaskAdmin(admin.ModelAdmin):  
    list_display = ('incidencia', 'descripcion', 'area', 'usuario', 'status', 'prioridad')  
    list_filter = ('area', 'status', 'prioridad')  
    search_fields = ('incidencia', 'descripcion')  
    filter_horizontal = ('tecnicos',)  

class PrioridadAdmin(admin.ModelAdmin):  
    list_display = ('nivel',)  
    search_fields = ('nivel',)  

class StatusAdmin(admin.ModelAdmin):  # Agregar una clase para administrar Status  
    list_display = ('estado',)  
    search_fields = ('estado',)  

# Registra los modelos en el panel de administración  
admin.site.register(Task, TaskAdmin)  
admin.site.register(Prioridad, PrioridadAdmin)  
admin.site.register(Status, StatusAdmin)  # Registrar el modelo Status