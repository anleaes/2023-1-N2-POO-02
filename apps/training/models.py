from django.db import models
#from student.models import Student
#from training import Training
#from instructor.models import Instructor
#from django.contrib.auth.models import User

# Create your models here.


class Training(models.Model):
    #student = models.ForeignKey(Student, on_delete=models.CASCADE)
    #instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    #training = models.ForeignKey(Training, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE) 
   
    class Meta:
        verbose_name = 'Training'
        verbose_name_plural = 'Trainings'
        ordering =['id']

    def __str__(self):
        return self.name