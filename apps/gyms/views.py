from django.shortcuts import render
from .models import Gyms
from rest_framework import viewsets
from .serializer import GymsSerializer

# Create your views here.

class GymsViewSet(viewsets.ModelViewSet):
    queryset = Gyms.objects.all()
    serializer_class = GymsSerializer  
