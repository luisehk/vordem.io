from django.apps import AppConfig


class EmailConfig(AppConfig):
    name = 'sealedair.apps.messaging.email'
    label = 'sealedair_email'

    def ready(self):
        pass
