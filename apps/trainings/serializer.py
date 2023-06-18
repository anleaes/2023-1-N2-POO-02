from .models import Trainings
from rest_framework import serializers

class TrainingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainings
        fields = '__all__'