from django.contrib import admin  

# Definición de clases administrativas  
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

# Función para registrar modelos  
def register_models():  
    from .models import Task, Prioridad, Status, Clasificacion  # Importar aquí para evitar circularidad  
    admin.site.register(Task, TaskAdmin)  
    admin.site.register(Prioridad, PrioridadAdmin)  
    admin.site.register(Status, StatusAdmin)  
    admin.site.register(Clasificacion, ClasificacionAdmin)  

# Ejecutar la función de registro  
register_models()