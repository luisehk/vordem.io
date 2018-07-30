from django.apps import AppConfig


class ProvidersConfig(AppConfig):
    name = 'sealedair.apps.providers'
    label = 'sealedair_providers'
    verbose_name = 'Proveedores'

    def ready(self):
        pass
