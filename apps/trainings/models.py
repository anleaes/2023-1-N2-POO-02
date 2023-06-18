from django.db import models
from students.models import Students
from exercises.models import Exercises
from gyms.models import Gyms

# Create your models here.

class Trainings(models.Model):
    date = models.CharField('Data', max_length=50)
    obs = models.TextField('Obs', max_length=100)
    exercises = models.ForeignKey(Exercises, on_delete=models.CASCADE)
    gyms = models.ForeignKey(Gyms, on_delete=models.CASCADE)
    students = models.ForeignKey(Students, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Treino'
        verbose_name_plural = 'Treinos'
        ordering =['id']

    def __str__(self):
        return self.date