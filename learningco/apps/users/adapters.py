from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.signals import pre_social_login
from allauth.account.utils import perform_login
from django.dispatch import receiver


User = get_user_model()


class AccountAdapter(DefaultAccountAdapter):
    pass


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        pass


@receiver(pre_social_login)
def link_to_local_user(sender, request, sociallogin, **kwargs):
    """
        Capture user email when signin up through a soccial account.
        If a user with that email already exists, log that user in.
    """

    email_key = ''

    if sociallogin.account.provider in ('facebook', 'twitter'):
        email_key = 'email'
    elif sociallogin.account.provider == 'linkedin':
        email_key = 'email-address'

    if email_key:
        email_address = sociallogin.account.extra_data[email_key]

        user = User.objects.filter(email=email_address)
        if user.exists():
            perform_login(
                request,
                user[0],
                email_verification=settings.ACCOUNT_EMAIL_VERIFICATION)
            raise ImmediateHttpResponse(redirect('/'))
