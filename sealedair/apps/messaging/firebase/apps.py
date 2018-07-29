from django.db.models.signals import post_save
from django.apps import AppConfig


class FirebaseConfig(AppConfig):
    name = 'sealedair.apps.messaging.firebase'
    label = 'sealedair_firebase'

    def ready(self):
        from sealedair.apps.messaging.firebase.signals import \
            send_push_notification
        from notifications.models import Notification

        post_save.connect(send_push_notification, sender=Notification)
