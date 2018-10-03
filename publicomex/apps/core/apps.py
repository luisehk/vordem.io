from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'publicomex.apps.core'
    label = 'publicomex_core'
    verbose_name = 'Core'

    def ready(self):
        pass
