from django.db import models

# Create your models here.

from training.models import Training
from planfood.models import PlanFood
from django.contrib.auth.models import User

class Student(models.Model):
    objetivo = models.CharField('objetivo', max_length=100)
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    foodplan = models.ForeignKey(PlanFood, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.objetivo