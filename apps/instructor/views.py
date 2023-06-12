from django.shortcuts import render
from .models import Instructor
from rest_framework import viewsets
from .serializer import InstructorSerializer

# Create your views here.

class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer  