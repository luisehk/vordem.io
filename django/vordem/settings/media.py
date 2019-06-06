import os
from .default import BASE_DIR, LOCAL

# static and media files
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

if not os.environ.get('AWS_ACCESS_KEY_ID', None):
    # serve media/static files through local server
    USING_S3 = False
    STATIC_URL = '/static/' if not LOCAL else '/local-static/'
    STATIC_ROOT = os.path.join(
        BASE_DIR,
        '.static/'
    )

    MEDIA_ROOT = os.path.join(BASE_DIR, '.media/')
    MEDIA_URL = os.environ.get('MEDIA_URL', '/media/')
else:
    # serve media/static files through amazon s3
    USING_S3 = True
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_QUERYSTRING_AUTH = False

    STATICFILES_LOCATION = 'static'
    STATIC_URL = 'https://s3.amazonaws.com/{}/{}/'.format(
        AWS_STORAGE_BUCKET_NAME, STATICFILES_LOCATION)
    STATICFILES_STORAGE = 'vordem.storages.StaticStorage'

    MEDIAFILES_LOCATION = 'media'
    MEDIA_URL = 'https://s3.amazonaws.com/{}/{}/'.format(
        AWS_STORAGE_BUCKET_NAME, MEDIAFILES_LOCATION)
    DEFAULT_FILE_STORAGE = 'vordem.storages.MediaStorage'

    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
