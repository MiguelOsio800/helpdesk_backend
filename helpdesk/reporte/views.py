from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ReporteSerializer

# Create your views here.

class ReporteViewSet(viewsets.ModelViewSet):
    queryset = ReporteSerializer.Meta.model.objects.all()
    serializer_class = ReporteSerializer

