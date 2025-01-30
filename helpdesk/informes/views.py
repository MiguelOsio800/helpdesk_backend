from rest_framework import viewsets, status  
from rest_framework.decorators import api_view  
from rest_framework.response import Response  
from django.shortcuts import get_object_or_404  
from .models import Informe  
from tasks.models import Task, Status  # Asegúrate de importar Status  
from .serializers import InformeSerializer  

class ReporteViewSet(viewsets.ModelViewSet):  
    queryset = Informe.objects.all()  
    serializer_class = InformeSerializer  

class ReporteViewSet(viewsets.ModelViewSet):  
    queryset = Informe.objects.all()  
    serializer_class = InformeSerializer  

    ########################################################
    ###########            CREATE             ##############
    ########################################################



    def create(self, request, *args, **kwargs):  
        print(request.data)  
        consulta_tasks = Task.objects.filter(id=request.data['task'])  
        print(consulta_tasks.values('tecnicos'))  
        
        # Inicializamos la variable para validar el estado de los informes  
        validar_status = False  
        tecnicos_ids = []  # Para almacenar los IDs de los técnicos  

        # Obtenemos los IDs de los técnicos de la tarea  
        for tecnico in consulta_tasks.values('tecnicos'):  
            tecnico_id = tecnico['tecnicos']  
            tecnicos_ids.append(tecnico_id)  
            print('tecnicos:', tecnico_id)  
            print('tasks:', request.data['task'])  
            
            # Consultamos informes existentes para cada técnico  
            consulta_reporte = Informe.objects.filter(task=request.data['task'], usuario=tecnico_id)  
            print('consulta_reporte:', consulta_reporte)  
            
            if consulta_reporte.exists():  
                print('Ya reportó')  
            else:  
                print('No reportó')  
                validar_status = True  # Al menos un informe falta  

        print('validar_status:', validar_status)  

        # Guardamos el estado de la tarea según los informes generados  
        ticket = consulta_tasks.first()  # Obtenemos la primera tarea  

        if validar_status:  
            print('Al menos un informe falta. Estado de la tarea: "En Proceso".')  
            ticket.status = Status.objects.get(estado='En Proceso')  # Asignamos estado "En Proceso"  
        else:  
            print('Todos los informes han sido generados. Estado de la tarea: "Para Revisión".')  
            ticket.status = Status.objects.get(estado='Para Revisión')  # Asignamos estado "Para Revisión"  

        ticket.save()  # Guardamos los cambios en la base de datos  
            
        serializer = self.get_serializer(data=request.data)  
        serializer.is_valid(raise_exception=True)  
        self.perform_create(serializer)  
        headers = self.get_success_headers(serializer.data)  
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    ########################################################
    ###########            UPDATE             ##############
    ########################################################
    
    def update(self, request, *args, **kwargs):  
        # Primero, llamamos a la función de actualización base  
        partial = kwargs.pop('partial', False)  # Permite actualizar parcialmente  
        instance = self.get_object()  # Obtenemos el objeto actual a actualizar  
        serializer = self.get_serializer(instance, data=request.data, partial=partial)  
        serializer.is_valid(raise_exception=True)  

        # Realizamos la actualización del informe  
        self.perform_update(serializer)  

        # Ahora verificamos el estado de los informes  
        consulta_tasks = Task.objects.filter(id=instance.task.id)  # Obtenemos la tarea relacionada  
        print(consulta_tasks.values('tecnicos'))  
        
        validar_status = False  
        for tecnico in consulta_tasks.values('tecnicos'):  
            tecnico_id = tecnico['tecnicos']  
            print('tecnicos:', tecnico_id)  
            print('tasks:', instance.task.id)  

            # Consultamos informes existentes para cada técnico  
            consulta_reporte = Informe.objects.filter(task=instance.task, usuario=tecnico_id)  
            print('consulta_reporte:', consulta_reporte)  

            if consulta_reporte.exists():  
                print('Ya reportó')  
            else:  
                print('No reportó')  
                validar_status = True  # Al menos un informe falta  
        
        print('validar_status:', validar_status)  

        # Guardamos el estado de la tarea según los informes generados  
        ticket = consulta_tasks.first()  # Obtenemos la primera tarea  

        if validar_status:  
            print('Al menos un informe falta. Estado de la tarea: "En Proceso".')  
            ticket.status = Status.objects.get(estado='En Proceso')  
        else:  
            print('Todos los informes han sido generados. Estado de la tarea: "Para Revisión".')  
            ticket.status = Status.objects.get(estado='Para Revisión')  

        ticket.save()  # Guardamos los cambios en la base de datos  
            
        headers = self.get_success_headers(serializer.data)  
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)  