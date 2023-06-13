from django.db import models

# Create your models here.
class PlanFood(models.Model):
    alimento = models.CharField('alimento', max_length=200)
    quantidade = models.TextField('quantidade', max_length=15)
    
    class Meta:
        verbose_name = 'PlanFood'
        verbose_name_plural = 'PlanFoods'
        ordering =['id']

    def __str__(self):
        return self.name