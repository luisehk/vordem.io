from django.db.models import ForeignKey, CharField
from django.contrib.auth import get_user_model
from fcm.models import AbstractDevice

User = get_user_model()


class CustomDevice(AbstractDevice):
    user = ForeignKey(User)
    dev_id = CharField(verbose_name='Device ID', null=True, blank=True,
                       max_length=50, unique=True,)

    def __str__(self):
        # Repr function fails if we remove this. I don't know why
        return 'DEV_ID: {}'.format(
            self.dev_id
        ) if self.dev_id else 'PK: {}'.format(
            self.pk
        )
