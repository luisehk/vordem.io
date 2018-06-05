import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
LOCAL = os.environ.get('LOCAL', 'False').lower() == 'true'
SHOW_DEBUG_TOOLBAR = os.environ.get(
    'SHOW_DEBUG_TOOLBAR', 'False').lower() == 'true'

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'debug_toolbar',

    'allauth',
    'allauth.account',

    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'rest_framework_docs',
    'rest_framework_swagger',

    'django_filters',
    'django_comments',
    'taggit',
    'taggit_templatetags2',

    'ckeditor',
    'colorfield',
    'versatileimagefield',
    'embed_video',

    'djcelery_email',
    'cacheops',
    'fcm',
    'corsheaders',

    'notifications',

    'learningco.apps.admin',
    'learningco.apps.content',
    'learningco.apps.companies',
    'learningco.apps.messaging.email',
    'learningco.apps.messaging.firebase',
    'learningco.apps.progress',
    'learningco.apps.score',
    'learningco.apps.users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'crum.CurrentRequestUserMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.static',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.tz',
            ],
        },
    },
]

# general settings
WSGI_APPLICATION = 'learningco.wsgi.application'
ROOT_URLCONF = 'learningco.urls'
SITE_ID = 1
TAGGIT_CASE_INSENSITIVE = True

# static and media files
STATIC_URL = '/static/' if not LOCAL else '/local-static/'
STATIC_ROOT = os.path.join(
    BASE_DIR,
    '.static/'
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
