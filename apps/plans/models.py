from django.db import models

from students.models import Students

# Create your models here.

class Plans(models.Model):
    food = models.CharField('Alimento', max_length=50)
    quantity = models.TextField('Quantidade', max_length=100)
    Students = models.ForeignKey(Students, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Plans'
        ordering =['id']

    def __str__(self):
        return self.food