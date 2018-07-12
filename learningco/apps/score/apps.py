from django.db.models.signals import post_save
from django.apps import AppConfig


class ScoreConfig(AppConfig):
    name = 'learningco.apps.score'
    label = 'learningco_score'

    def ready(self):
        from django.contrib.auth import get_user_model
        from learningco.apps.companies.models import Company
        from learningco.apps.content.models import Skill
        from learningco.apps.score.signals import (
            create_company_score, create_company_skill_score,
            create_leader_score, create_leader_skill_score,
            create_skill_leader_score, create_skill_company_score,)

        User = get_user_model()

        post_save.connect(create_company_score, sender=Company)
        post_save.connect(create_company_skill_score, sender=Company)
        post_save.connect(create_leader_score, sender=User)
        post_save.connect(create_leader_skill_score, sender=User)
        post_save.connect(create_skill_leader_score, sender=Skill)
        post_save.connect(create_skill_company_score, sender=Skill)
