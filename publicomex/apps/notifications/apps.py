from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    name = 'publicomex.apps.notifications'
    label = 'publicomex_notifications'
    verbose_name = 'Notifications'

    def ready(self):
        pass
