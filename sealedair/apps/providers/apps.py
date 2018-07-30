from django.apps import AppConfig


class ProvidersConfig(AppConfig):
    name = 'sealedair.apps.providers'
    label = 'sealedair_providers'

    def ready(self):
        pass
