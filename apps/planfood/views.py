from django.shortcuts import render
from .models import PlanFood
from rest_framework import viewsets
from .serializer import CategorySerializer

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = PlanFood.objects.all()
    serializer_class = CategorySerializer  