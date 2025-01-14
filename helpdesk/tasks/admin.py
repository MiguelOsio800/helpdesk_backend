from django.contrib import admin  
from .models import Task, Prioridad, Status, Clasificacion  

class TaskAdmin(admin.ModelAdmin):  
    list_display = ('incidencia', 'descripcion', 'fecha_creacion', 'fecha_final', 'area', 'usuario', 'status', 'prioridad', 'clasificacion')  # Incluye ambas fechas  
    list_filter = ('area', 'status', 'prioridad', 'fecha_creacion', 'fecha_final')  # Filtra por ambas fechas  
    search_fields = ('incidencia', 'descripcion')  
    filter_horizontal = ('tecnicos',)  

class PrioridadAdmin(admin.ModelAdmin):  
    list_display = ('nivel',)  
    search_fields = ('nivel',)  

class StatusAdmin(admin.ModelAdmin):  
    list_display = ('estado',)  
    search_fields = ('estado',)  

class ClasificacionAdmin(admin.ModelAdmin):  
    list_display = ('clasificacion',)  # Cambiado de 'tema' a 'clasificacion'  
    search_fields = ('clasificacion',)  # Cambiado de 'tema' a 'clasificacion'  

admin.site.register(Task, TaskAdmin)  
admin.site.register(Prioridad, PrioridadAdmin)  
admin.site.register(Status, StatusAdmin)  
admin.site.register(Clasificacion, ClasificacionAdmin)