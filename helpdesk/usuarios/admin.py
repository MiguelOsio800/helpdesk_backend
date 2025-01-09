# admin.py  
from django.contrib import admin  
from .models import Usuario, Area  

class UsuarioAdmin(admin.ModelAdmin):  
    list_display = ('nombres', 'apellidos', 'area', 'correo', 'rol')  # Campos que se mostrarán en la lista  
    search_fields = ('nombres', 'apellidos', 'correo')  # Campos que se pueden buscar  
    list_filter = ('rol', 'area')  # Permite filtrar por rol y área en el panel  

admin.site.register(Usuario, UsuarioAdmin)  
admin.site.register(Area)