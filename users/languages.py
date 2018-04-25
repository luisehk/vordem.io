from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from crum import get_current_request


ENGLISH_CODE = 'en'
SPANISH_CODE = 'es'

LANGUAGE = (
    (ENGLISH_CODE, _('English')),
    (SPANISH_CODE, _('Spanish')),
)


def set_language(language):
    request = get_current_request()
    if request is not None:
        translation.activate(language)
        request.session[translation.LANGUAGE_SESSION_KEY] = language
        request.LANGUAGE_CODE = translation.get_language()
