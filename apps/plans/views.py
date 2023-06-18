from django.shortcuts import render

# Create your views here.

from .models import Plans
from rest_framework import viewsets
from .serializer import PlansSerializer

# Após o comentario "# Create your views here." e crie as views "Product".

class PlansViewSet(viewsets.ModelViewSet):
    queryset = Plans.objects.all()
    serializer_class = PlansSerializer  