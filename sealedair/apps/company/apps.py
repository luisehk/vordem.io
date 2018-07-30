from django.apps import AppConfig


class CompanyConfig(AppConfig):
    name = 'sealedair.apps.company'
    label = 'sealedair_company'

    def ready(self):
        pass
