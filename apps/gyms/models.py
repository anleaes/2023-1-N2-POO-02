from django.db import models

# Create your models here.

class Gyms(models.Model):
    name = models.CharField('Nome', max_length=50)
    address = models.TextField('Endereco', max_length=100)
    cnpj = models.TextField('CNPJ', max_length=100)
    
    class Meta:
        verbose_name = 'Academia'
        verbose_name_plural = 'Academias'
        ordering =['id']

    def __str__(self):
        return self.name