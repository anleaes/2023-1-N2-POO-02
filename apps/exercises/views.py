from django.shortcuts import render


from .models import Exercises
from rest_framework import viewsets
from .serializer import ExercisesSerializer

# Create your views here.

class ExercisesViewSet(viewsets.ModelViewSet):
    queryset = Exercises.objects.all()
    serializer_class = ExercisesSerializer  