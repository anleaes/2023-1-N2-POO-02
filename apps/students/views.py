from django.shortcuts import render

from .models import Students
from rest_framework import viewsets
from .serializer import StudentsSerializer

# Create your views here.

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer  