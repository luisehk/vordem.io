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
    STATIC_URL = '/static/' if not LOCAL else '/local-static/'
    STATIC_ROOT = os.path.join(
        BASE_DIR,
        '.static/'
    )

    MEDIA_ROOT = os.path.join(BASE_DIR, '.media/')
    MEDIA_URL = os.environ.get('MEDIA_URL', '/media/')
    USING_S3 = False
else:
    # serve media/static files through amazon s3
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_QUERYSTRING_AUTH = False

    STATICFILES_LOCATION = 'static'
    STATIC_URL = 'https://s3.amazonaws.com/{}/{}/'.format(
        AWS_STORAGE_BUCKET_NAME, STATICFILES_LOCATION)
    STATICFILES_STORAGE = 'publicomex.storages.StaticStorage'

    MEDIAFILES_LOCATION = 'media'
    MEDIA_URL = 'https://s3.amazonaws.com/{}/{}/'.format(
        AWS_STORAGE_BUCKET_NAME, MEDIAFILES_LOCATION)
    DEFAULT_FILE_STORAGE = 'publicomex.storages.MediaStorage'

    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }

    USING_S3 = True

VERSATILEIMAGEFIELD_SETTINGS = {
    'cache_length': 2592000,
    'cache_name': 'versatileimagefield_cache',
    'jpeg_resize_quality': 85,
    'sized_directory_name': '__sized__',
    'filtered_directory_name': '__filtered__',
    'placeholder_directory_name': '__placeholder__',
    'create_images_on_demand': False,
    'image_key_post_processor': None,
    'progressive_jpeg': True
}

VERSATILEIMAGEFIELD_USE_PLACEHOLDIT = True
VERSATILEIMAGEFIELD_RENDITION_KEY_SETS = {
    'profile_avatar': [
        ('full_size', 'url'),
        ('crop__400x400', 'crop__400x400'),
        ('crop__280x280', 'crop__280x280'),
        ('crop__128x128', 'crop__128x128'),
        ('crop__44x44', 'crop__44x44'),
        ('crop__42x42', 'crop__42x42'),
    ]
}
