from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
import os


def send_email(subject='', to_email=[], template='', ctx={}):
        from_email = os.environ.get("DEFAULT_FROM_EMAIL")
        message = get_template(template).render(ctx)
        msg = EmailMultiAlternatives(
            subject, message, to=to_email, from_email=from_email)
        msg.content_subtype = 'html'
        msg.send()
