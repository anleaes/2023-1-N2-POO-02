from .models import PlanFood
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanFood
        fields = '__all__'
        
        # Para chamar todos os atributos:
        # fields = '__all__'
        
        # Para chamar somentes os atributos de interesse:
        # fields = ['id','created_on', 'updated_on', 'name', 'description']