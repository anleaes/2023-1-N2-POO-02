from django.shortcuts import render
from .models import Exercises
from rest_framework import viewsets
from .serializer import CategorySerializer

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Exercises.objects.all()
    serializer_class = CategorySerializer