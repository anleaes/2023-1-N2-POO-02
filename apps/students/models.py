from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField('Nome', max_length=50)
    address = models.TextField('Endereco', max_length=100)
    fone = models.TextField('Fone', max_length=100)

    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering =['id']

    def __str__(self):
        return self.name
