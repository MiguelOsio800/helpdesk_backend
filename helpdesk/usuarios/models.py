###############################################  
##### Modelos para El Sistema De Usuarios #####  
###############################################  

from django.db import models  # Importamos el módulo models de Django  
from django.contrib.auth.models import AbstractUser, UserManager  # Importamos AbstractUser y UserManager para usuario personalizado  
# No es necesario importar make_password, usaremos set_password para el manejo de contraseñas.  

##################################  
##### Clase Area #################  
##################################  
class Area(models.Model):  
    nombre = models.CharField(max_length=100)  # Campo para el nombre del área  

    def __str__(self):  
        return self.nombre  # Representación en cadena del objeto  

    class Meta:  
        verbose_name_plural = "Area"  # Nombre plural en el panel de administración  

##################################  
##### Clase Rol ##################  
##################################  
class Rol(models.Model):  
    nombre = models.CharField(max_length=50, unique=True)  # Campo para el nombre del rol (único)  

    def __str__(self):  
        return self.nombre  # Representación en cadena del objeto  

    class Meta:  
        verbose_name_plural = "Rol"  # Nombre plural en el panel de administración  

##################################  
##### Clase Usuario ##############  
##################################  
class Usuario(AbstractUser):  
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='usuarios', null=True)  # Relación con el modelo Area  
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name='usuarios', null=True)  # Relación con el modelo Rol  

    objects = UserManager()  # Añadido para acceder al método create_user  

    def __str__(self):  
        return f"{self.first_name} {self.last_name} - {self.rol.nombre if self.rol else 'Sin rol'}"  # Representación en cadena del objeto  

    class Meta:  
        verbose_name_plural = "Usuario"  # Nombre plural en el panel de administración  

    @classmethod  
    def crear_usuario(cls, username, password, first_name='', last_name='', area=None, rol=None):  
        # Método para crear un nuevo usuario  
        usuario = cls(  
            username=username,  
            first_name=first_name,  
            last_name=last_name,  
            area=area,  
            rol=rol,  
            is_active=True  # Asegúrate de que el usuario esté activo  
        )  
        usuario.set_password(password)  # Establece la contraseña con hashing  
        usuario.save()  # Guarda el usuario en la base de datos  
        return usuario  # Retorna el usuario creado  

##################################  
##### Clase Clasificacion ########  
##################################  
class Clasificacion(models.Model):  
    nombre = models.CharField(max_length=100)  # Campo para el nombre de la clasificación  

    def __str__(self):  
        return self.nombre  # Representación en cadena del objeto  

    class Meta:  
        verbose_name_plural = "Clasificacion"  # Nombre plural en el panel de administración  

##################################  
##### Clase Task #################   
##################################  
class Task(models.Model):  
    titulo = models.CharField(max_length=200)  # Campo para el título de la tarea  
    clasificacion = models.ForeignKey(Clasificacion, on_delete=models.CASCADE, related_name='tasks')  # Relación con el modelo Clasificacion  
    usuario_asignado = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tasks')  # Relación con el modelo Usuario  

    def __str__(self):  
        return f"{self.titulo} - {self.clasificacion.nombre if self.clasificacion else 'Sin clasificacion'}"  # Representación en cadena del objeto  

    class Meta:  
        verbose_name_plural = "Task"  # Nombre plural en el panel de administración