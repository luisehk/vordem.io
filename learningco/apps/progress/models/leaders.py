from django.contrib.auth import get_user_model
from ...content.models import Skill, Lesson
from django.db import models


User = get_user_model()


class LessonCompletion(models.Model):
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE)
    leader = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
