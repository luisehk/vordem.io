from django.contrib.auth import get_user_model
from colorfield.fields import ColorField
from django.db import models


User = get_user_model()


class Plant(models.Model):
    name = models.CharField(
        verbose_name='Nombre',
        max_length=150)
    code = models.CharField(
        verbose_name='Código',
        max_length=4)
    color = ColorField(
        verbose_name='Color',
        default='#FF0000')

    class Meta:
        verbose_name = 'planta'
        verbose_name_plural = 'plantas'
        ordering = ['name']

    def __str__(self):
        return self.name
