from django.db import models

# Create your models here.
class Food_Plan(models.Model):
    alimento = models.CharField('alimento', max_length=200)
    quantidade = models.TextField('quantidade', max_length=15)
    
    class Meta:
        verbose_name = 'Plan_food'
        verbose_name_plural = 'Plan_foods'
        ordering =['id']

    def __str__(self):
        return self.name