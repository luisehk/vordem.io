from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Skill(models.Model):
    name = models.CharField(
        verbose_name='Nombre',
        max_length=150)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
