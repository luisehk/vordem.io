from django.contrib.auth import get_user_model
from django.db import models
from .skills import Skill


User = get_user_model()


class Lesson(models.Model):
    skill = models.ForeignKey(
        Skill, verbose_name='Competencia',
        null=True, blank=True,
        on_delete=models.CASCADE)
    name = models.CharField(
        verbose_name='Nombre',
        max_length=150)
    default = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
