from django.db import models

# Create your models here.

from student.models import Student
from instructor.models import Instructor
class Gym(models.Model):
    nome = models.CharField('nome', max_length=50)
    adress = models.CharField('adress', max_length=50)
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