from django.apps import AppConfig


class CompanyConfig(AppConfig):
    name = 'sealedair.apps.company'
    label = 'sealedair_company'
    verbose_name = 'Sealed Air'

    def ready(self):
        pass
