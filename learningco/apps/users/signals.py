from django.utils.translation import ugettext as _
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from crum import get_current_request
from ..messaging.email.helpers import send_email
from .models import Profile


User = get_user_model()


def create_user_profile(sender, **kwargs):
    u = kwargs['instance']

    if not Profile.objects.filter(user=u).exists():
        Profile.objects.create(user=u)


def set_email_as_username(sender, **kwargs):
    u = kwargs['instance']

    # cleanup email
    modified = False
    email = u.email
    email = email.strip()
    email = email.lower()

    if email != u.email:
        u.email = email
        modified = True

    if u.username != u.email:
        u.username = u.email
        modified = True

    if modified:
        u.save()


def warm_user_profile_avatar(sender, **kwargs):
    p = kwargs['instance']
    p.warm_avatar()


def notify_user_creation(sender, **kwargs):
    if kwargs.get('created', False):
        user = kwargs.get('instance', None)
        password = ''  # nosec

        if not user.has_usable_password():
            # Disconnect signal to avoid transaction abortion
            post_save.disconnect(receiver=notify_user_creation, sender=sender)
            password = User.objects.make_random_password()
            user.set_password(password)
            user.save()

            # reconnect the signal
            post_save.connect(notify_user_creation, sender=User)

        send_email(
            subject=_('Bienvenido to Learningco'),
            to_email=[user.email],
            template='emails/welcome.html',
            ctx={
                'user': user.email,
                'password': password,
                'request': get_current_request()
            })
