from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    name = 'sealedair.apps.notifications'
    label = 'sealedair_notifications'
    verbose_name = 'Notificaciones'

    def ready(self):
        pass
