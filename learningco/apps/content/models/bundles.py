from django.db import models
from .skills import Skill
from .lessons import Intro, Video, Article, ActivityList, Quiz
from ...users.models import Profile


class Bundle(models.Model):
    skill = models.ForeignKey(
        Skill, verbose_name='Competencia',
        null=False, on_delete=models.CASCADE,
        related_name='bundles')
    name = models.CharField(max_length=150)
    intro = models.ForeignKey(
        Intro, null=True, on_delete=models.SET_NULL,
        related_name='intro_bundles')
    video = models.ForeignKey(
        Video, null=True, on_delete=models.SET_NULL,
        related_name='video_bundles')
    article = models.ForeignKey(
        Article, null=True, on_delete=models.SET_NULL,
        related_name='article_bundles')
    activity_list = models.ForeignKey(
        ActivityList, null=True, on_delete=models.SET_NULL,
        related_name='activity_list_bundles')
    quiz = models.ForeignKey(
        Quiz, null=True, on_delete=models.SET_NULL,
        related_name='quiz_bundles')

    generation = models.CharField(
        max_length=2, choices=Profile.GENERATIONS,
        default=Profile.MILLENIALS)
    level_of_hierarchy = models.CharField(
        max_length=3, choices=Profile.LEVELS_OF_HIERARCHY,
        default=Profile.OPERATION_LEVEL_EMPLOYEE)

    class Meta:
        unique_together = (
            ('skill', 'generation', 'level_of_hierarchy'),
        )
