from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    name = 'sealedair.apps.notifications'
    label = 'sealedair_notifications'

    def ready(self):
        pass
