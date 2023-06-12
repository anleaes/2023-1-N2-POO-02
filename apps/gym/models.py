from django.db import models
from gym.models import Gym
# Create your models here.

from student.models import Student
from instructor.models import Instructor
class gym(models.Model):
    cnpj = models.CharField('cnpj', max_length=50)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    class Meta:
        verbose_name = 'Gym'
        verbose_name_plural = 'Gyms'
        ordering =['id']

    def __str__(self):
        return self.name