from django.db.models.signals import post_save
from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'sealedair.apps.users'
    label = 'sealedair_users'

    def ready(self):
        from django.contrib.auth import get_user_model
        from sealedair.apps.users.models import Profile
        from sealedair.apps.users.signals import (
            create_user_profile, warm_user_profile_avatar,
            set_email_as_username, notify_user_creation,
        )

        User = get_user_model()

        post_save.connect(create_user_profile, sender=User)
        post_save.connect(warm_user_profile_avatar, sender=Profile)
        post_save.connect(set_email_as_username, sender=User)
        post_save.connect(notify_user_creation, sender=User)
