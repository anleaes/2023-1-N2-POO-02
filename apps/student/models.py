from django.db import models

# Create your models here.

from training.models import Training
from plan_food.models import Plan_food
from django.contrib.auth.models import User

class Student(models.Model):
    objetivo = models.CharField('objetivo', max_length=100)
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    food_plan = models.ForeignKey(Plan_food, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.objetivo