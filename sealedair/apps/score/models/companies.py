from django.contrib.auth import get_user_model
from ...companies.models import Company
from ...content.models import Skill
from django.db import models


User = get_user_model()


class CompanyScore(models.Model):
    company = models.OneToOneField(
        Company,
        on_delete=models.CASCADE,
        related_name='company_score')
    score_before = models.IntegerField(default=0)
    score_now = models.IntegerField(default=0)


class CompanySkillScore(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='company_skill_scores')
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE)
    score_before = models.IntegerField(default=0)
    score_now = models.IntegerField(default=0)

    class Meta:
        unique_together = (('company', 'skill'),)
