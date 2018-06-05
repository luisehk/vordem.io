from django.contrib.auth import get_user_model
from ...content.models import Skill, Lesson, Question, Option
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


class QuizCompletion(LessonCompletion):
    quiz_score = models.IntegerField(default=0)


class QuizAnswer(models.Model):
    quiz_completion = models.ForeignKey(
        QuizCompletion,
        on_delete=models.CASCADE)
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE)
    option = models.ForeignKey(
        Option,
        on_delete=models.CASCADE)
    leader = models.ForeignKey(
        User,
        on_delete=models.CASCADE)


class SkillCompletion(models.Model):
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE)
    leader = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    comment = models.TextField()
