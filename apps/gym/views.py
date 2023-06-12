from django.shortcuts import render
from .models import Gym
from rest_framework import viewsets
from .serializer import ProductSerializer
# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = ProductSerializer  