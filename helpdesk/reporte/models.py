from django.db import models

# Create your models here.

class Reportes(models.Model):  
    reportes = models.CharField(max_length=200, unique=True)  # Cambiar 'Reportes' a 'reportes' en minúsculas  

    def __str__(self):  
        return self.reportes  # Cambiar 'self.tema' a 'self.reportes'  

    class Meta:  
        verbose_name_plural = "Reportes"  