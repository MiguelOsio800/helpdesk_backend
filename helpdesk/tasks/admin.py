from django.contrib import admin  
from .models import Task, Prioridad, Status, Clasificacion, Informe 

class TaskAdmin(admin.ModelAdmin):  
    list_display = ('incidencia', 'descripcion', 'fecha_creacion', 'fecha_final', 'area', 'usuario', 'status', 'prioridad', 'clasificacion')  
    list_filter = ('area', 'status', 'prioridad', 'fecha_creacion', 'fecha_final')  
    search_fields = ('incidencia', 'descripcion')  
    filter_horizontal = ('tecnicos',)  

class PrioridadAdmin(admin.ModelAdmin):  
    list_display = ('nivel',)  
    search_fields = ('nivel',)  

class StatusAdmin(admin.ModelAdmin):  
    list_display = ('estado',)  
    search_fields = ('estado',)  

class ClasificacionAdmin(admin.ModelAdmin):  
    list_display = ('clasificacion',)  
    search_fields = ('clasificacion',)  

class InformeAdmin(admin.ModelAdmin): 
    list_display = ('task', 'area', 'usuario', 'equipo', 'numero_de_bien', 'motivo', 'solucion', 'status', 'observacion', 'completado') 
    search_fields = ('task__incidencia', 'usuario__username', 'status') 
    list_filter = ('status', 'completado')

admin.site.register(Informe, InformeAdmin)
admin.site.register(Task, TaskAdmin)  
admin.site.register(Prioridad, PrioridadAdmin)  
admin.site.register(Status, StatusAdmin)  
admin.site.register(Clasificacion, ClasificacionAdmin)