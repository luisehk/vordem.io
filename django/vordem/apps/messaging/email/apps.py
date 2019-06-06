from django.apps import AppConfig


class EmailConfig(AppConfig):
    name = 'vordem.apps.messaging.email'
    label = 'vordem_email'

    def ready(self):
        pass
