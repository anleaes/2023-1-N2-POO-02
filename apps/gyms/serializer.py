from .models import Gyms
from rest_framework import serializers

class GymsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gyms
        fields = '__all__'