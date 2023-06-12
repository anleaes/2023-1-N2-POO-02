from .models import Gym
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = '__all__'