from django.db import models

# Create your models here.

class Exercises(models.Model):
    tipo_exercicio = models.CharField('tipo_exercicio', max_length=150)
    peso = models.CharField('peso', max_length=3)
    repeticoes = models.TextField('repeticoes', max_length=3)
    
    class Meta:
        verbose_name = 'Exercises'
        verbose_name_plural = 'Exercises'
        ordering =['id']

    def __str__(self):
        return self.tipo_exercicio
        

