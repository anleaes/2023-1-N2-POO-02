from django.shortcuts import render
from .models import Training
from rest_framework import viewsets
from .serializer import CategorySerializer

# Após o comentario "# Create your views here." e crie as views "Category".

class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = CategorySerializer  
