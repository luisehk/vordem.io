from django.db import models


class Industry(models.Model):
    name = models.CharField(
        verbose_name='Nombre', max_length=150)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
