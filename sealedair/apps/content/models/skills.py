from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Skill(models.Model):
    name = models.CharField(
        verbose_name='Nombre',
        max_length=150)
    intro = models.ForeignKey(
        'sealedair_content.Intro',
        null=True, on_delete=models.SET_NULL,
        related_name='intro_skills')
    video = models.ForeignKey(
        'sealedair_content.Video',
        null=True, on_delete=models.SET_NULL,
        related_name='video_skills')
    article = models.ForeignKey(
        'sealedair_content.Article',
        null=True, on_delete=models.SET_NULL,
        related_name='article_skills')
    activity_list = models.ForeignKey(
        'sealedair_content.ActivityList',
        null=True, on_delete=models.SET_NULL,
        related_name='activity_list_skills')
    quiz = models.ForeignKey(
        'sealedair_content.Quiz',
        null=True, on_delete=models.SET_NULL,
        related_name='quiz_skills')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
