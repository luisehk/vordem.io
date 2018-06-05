from django.db import models
from .lessons import Lesson, Intro, Video, Article, ActivityList, Quiz


class Bundle(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=False)
    lessons = models.ManyToManyField(Lesson)
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
