from django.db import models

# Create your models here.

class Exercises(models.Model):
    type = models.TextField('Tipo', max_length=50)
    weigth = models.TextField('Descricao', max_length=100)
    hits = models.TextField('Repeticoes', max_length=100)

    
    class Meta:
        verbose_name = 'Exercises'
        verbose_name_plural = 'Exercises'
        ordering =['id']

    def __str__(self):
        return self.type