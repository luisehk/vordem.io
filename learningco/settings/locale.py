import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGE_CODE = 'es-MX'
LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)


def ugettext(s):
    return s


LANGUAGES = (
    ('es', ugettext('Spanish')),
)