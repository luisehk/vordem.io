from django.contrib.auth import get_user_model
from colorfield.fields import ColorField
from django.db import models


User = get_user_model()


class Carrier(models.Model):
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
        verbose_name = 'carrier'
        verbose_name_plural = 'carriers'
        ordering = ['name']

    def __str__(self):
        return self.name


class Truck(models.Model):
    carrier = models.ForeignKey(
        Carrier,
        verbose_name='Carrier',
        on_delete=models.CASCADE)
    code = models.CharField(
        verbose_name='Código',
        max_length=15)

    class Meta:
        verbose_name = 'camión'
        verbose_name_plural = 'camiones'
        ordering = ['code']

    def __str__(self):
        return self.code
