from django.contrib.auth import get_user_model
from ...content.models import Skill, Lesson
from django.db import models


User = get_user_model()


class LeaderScore(models.Model):
    leader = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='leader_score')
    score_before = models.IntegerField(default=0)
    score_now = models.IntegerField(default=0)


class LeaderSkillScore(models.Model):
    leader = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE)
    score_before = models.IntegerField(default=0)
    score_now = models.IntegerField(default=0)
    lessons = models.ManyToManyField(Lesson)
