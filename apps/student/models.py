from django.db import models

# Create your models here.

#from training.models import Training
from food_plan.models import Food_Plan
from django.contrib.auth.models import User

class Student(models.Model):
    objetivo = models.CharField('objetivo', max_length=100)
   # training = models.ForeignKey(Training, on_delete=models.CASCADE)
    food_plan = models.ForeignKey(Food_Plan, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
