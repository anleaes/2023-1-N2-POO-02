from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Instructor(models.Model):
    especialidade = models.CharField('Nome', max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.especialidade