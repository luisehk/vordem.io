from django.db.models.signals import post_save
from django.apps import AppConfig


class CompaniesConfig(AppConfig):
    name = 'sealedair.apps.companies'
    label = 'sealedair_companies'

    def ready(self):
        from sealedair.apps.companies.models import Company
        from sealedair.apps.companies.signals import \
            warm_company_profile_avatar

        post_save.connect(warm_company_profile_avatar, sender=Company)
