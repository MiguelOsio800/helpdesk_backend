from django.contrib import admin
from .models import Informe

class InformeAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista del administrador
    list_display = ('id', 'task', 'usuario', 'area', 'equipo', 'numero_de_bien', 'completado')

    # Campos por los que se podrá buscar
    search_fields = ('task__incidencia', 'usuario__username', 'equipo', 'numero_de_bien')

    # Opciones para filtrar en la vista de lista
    list_filter = ('completado', 'area')

    # Configuración opcional para organizar el formulario de edición
    fieldsets = (
        (None, {
            'fields': ('task', 'usuario', 'area', 'equipo', 'numero_de_bien', 'solucion', 'observacion', 'completado')
        }),
    )

# Registrar el modelo y el administrador personalizado
admin.site.register(Informe, InformeAdmin)
