from django.shortcuts import render
from .models import Plan_food
from rest_framework import viewsets
from .serializer import CategorySerializer

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Plan_food.objects.all()
    serializer_class = CategorySerializer  