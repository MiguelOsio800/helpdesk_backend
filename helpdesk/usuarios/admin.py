# admin.py  
from django.contrib import admin  
from .models import Usuario, Area, Rol  

class AreaAdmin(admin.ModelAdmin):  
    list_display = ('nombre',)  # Mostrar el nombre del área  
    search_fields = ('nombre',)  # Campo que se puede buscar  

class RolAdmin(admin.ModelAdmin):  
    list_display = ('nombre',)  # Mostrar el nombre del rol  
    search_fields = ('nombre',)  # Campo que se puede buscar  

class UsuarioAdmin(admin.ModelAdmin):  
    list_display = ('nombres', 'apellidos', 'area', 'correo', 'rol')  # Campos que se mostrarán en la lista  
    search_fields = ('nombres', 'apellidos', 'correo')  # Campos que se pueden buscar  
    list_filter = ('rol', 'area')  # Permitir filtrar por rol y área en el panel  

# Registro de modelos en el panel de administración  
admin.site.register(Usuario, UsuarioAdmin)  
admin.site.register(Area, AreaAdmin)  # Registrar el modelo Area  
admin.site.register(Rol, RolAdmin)  # Registrar el modelo Rol