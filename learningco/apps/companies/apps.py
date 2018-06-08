from django.db.models.signals import post_save
from django.apps import AppConfig


class CompaniesConfig(AppConfig):
    name = 'learningco.apps.companies'
    label = 'learningco_companies'

    def ready(self):
        from learningco.apps.companies.models import Company
        from learningco.apps.companies.signals import \
            warm_company_profile_avatar

        post_save.connect(warm_company_profile_avatar, sender=Company)
