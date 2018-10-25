import os
from .default import BASE_DIR

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGE_CODE = 'en-US'
LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)


def ugettext(s):
    return s


LANGUAGES = (
    ('en', ugettext('English')),
)
