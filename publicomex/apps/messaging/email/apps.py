from django.apps import AppConfig


class EmailConfig(AppConfig):
    name = 'publicomex.apps.messaging.email'
    label = 'publicomex_email'

    def ready(self):
        pass
