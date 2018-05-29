from django.contrib.auth import get_user_model
from embed_video.fields import EmbedVideoField
from django.db import models
from .skills import Skill


User = get_user_model()


class Lesson(models.Model):
    skill = models.ForeignKey(
        Skill, verbose_name='Competencia',
        null=False, on_delete=models.CASCADE,
        related_name='lessons')
    name = models.CharField(
        verbose_name='Nombre',
        max_length=150)
    default = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Intro(Lesson):
    body = models.TextField(blank=False)


class Video(Lesson):
    body = models.TextField(blank=False)
    video_url = EmbedVideoField()


class Quiz(Lesson):
    body = models.TextField(blank=False)


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz, verbose_name='Cuestionario',
        null=False, on_delete=models.CASCADE,
        related_name='questions')
    title = models.TextField(blank=False)


class Option(models.Model):
    question = models.ForeignKey(
        Question, verbose_name='Pregunta',
        null=False, on_delete=models.CASCADE,
        related_name='options')
    title = models.TextField(blank=False)
    value = models.IntegerField(default=0)


class Article(Lesson):
    description = models.TextField(blank=False)
    body = models.TextField(blank=False)
