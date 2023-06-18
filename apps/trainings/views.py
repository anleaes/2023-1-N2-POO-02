from django.shortcuts import render
from .models import Trainings
from rest_framework import viewsets
from .serializer import TrainingsSerializer

# Create your views here.

class TrainingsViewSet(viewsets.ModelViewSet):
    queryset = Trainings.objects.all()
    serializer_class = TrainingsSerializer  