from .models import Exercises
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercises
        fields = '__all__'