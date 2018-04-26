from django.apps import AppConfig


class EmailConfig(AppConfig):
    name = 'learningco.apps.messaging.email'
    label = 'learningco_email'

    def ready(self):
        pass
