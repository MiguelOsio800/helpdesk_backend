# admin.py  
from django.contrib import admin  
from .models import Usuario, Area, Rol  
from django.contrib.auth.admin import UserAdmin

class AreaAdmin(admin.ModelAdmin):  
    list_display = ('nombre',)  # Mostrar el nombre del área  
    search_fields = ('nombre',)  # Campo que se puede buscar  

class RolAdmin(admin.ModelAdmin):  
    list_display = ('nombre',)  # Mostrar el nombre del rol  
    search_fields = ('nombre',)  # Campo que se puede buscar  

class UsuarioAdmin(UserAdmin):  
    list_display = ('first_name', 'last_name', 'email', 'area', 'rol')  # Campos que se mostrarán en la lista  
    search_fields = ('first_name', 'last_name', 'email')  # Campos que se pueden buscar  
    list_filter = ('rol', 'area')  # Permitir filtrar por rol y área en el panel  
    
    fieldsets = UserAdmin.fieldsets + (  
        (None, {  
            'fields': ('area', 'rol')  # incluir los campos 'area' y 'rol'  
        }),  
    )  
    
    add_fieldsets = UserAdmin.add_fieldsets + (  
        (None, {  
            'fields': ('area', 'rol'),  # incluir los campos 'area' y 'rol'  
        }),  
    )  

# Registro de modelos en el panel de administración  
admin.site.register(Usuario, UsuarioAdmin)  # Asegúrate de usar UsuarioAdmin  
admin.site.register(Area, AreaAdmin)  # Registrar el modelo Area  
admin.site.register(Rol, RolAdmin)  # Registrar el modelo Rol