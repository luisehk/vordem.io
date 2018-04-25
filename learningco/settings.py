import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('SECRET_KEY', 'this-is-a-development-key')
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
ALLOWED_HOSTS = ['*']

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
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.linkedin_oauth2',
    'allauth.socialaccount.providers.twitter',

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

    'djcelery_email',
    'cacheops',
    'fcm',
    'corsheaders',

    'messaging.email',
    'messaging.firebase',
    'users',

    'notifications',
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
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
SITE_ID = 1
TAGGIT_CASE_INSENSITIVE = True

# language
LANGUAGE_CODE = 'en-US'
LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)


def ugettext(s):
    return s


LANGUAGES = (
    ('en', ugettext('English')),
    ('es', ugettext('Spanish')),
)

# headers
CORS_ORIGIN_ALLOW_ALL = True
USE_X_FORWARDED_HOST = True
CSRF_USE_SESSIONS = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# debugging
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda x: DEBUG,
}

ADMINS = []
admins = os.environ.get('ADMINS', '')
if admins:
    ADMINS = [
        (
            admin.strip(),
            admin.strip(),
        ) for admin in admins.strip(',').split(',')
    ]

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

# static and media files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '.static/')

MEDIA_ROOT = os.path.join(BASE_DIR, '.media/')
MEDIA_URL = os.environ.get('MEDIA_URL', '/media/')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# databases
DATABASES = {
    # heroku or docker
    'default': dj_database_url.config(engine='django_postgrespool')
} if os.environ.get('DATABASE_URL', '') else {
    # localhost
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# celery
CELERY_BROKER_URL = os.environ.get('REDIS_URL', 'redis://redis:6379/0')
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = TIME_ZONE
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# email
EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
CELERY_EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'bot@vordem.mx')
SERVER_EMAIL = DEFAULT_FROM_EMAIL

if os.environ.get('EMAIL_HOST_USER', ''):
    CELERY_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'user')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'password')
    EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
    EMAIL_PORT = int(os.environ.get('EMAIL_PORT', '587'))
    EMAIL_TIMEOUT = int(os.environ.get('EMAIL_TIMEOUT', '30'))
    EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True').lower() == 'true'
    EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL', 'False').lower() == 'true'

# push notifications
FCM_APIKEY = os.environ.get('FCM_APIKEY', '')
FCM_DEVICE_MODEL = 'firebase.CustomDevice'
FCM_MAX_RECIPIENTS = 1000

# authentication
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_LOGOUT_ON_GET = True
SOCIALACCOUNT_EMAIL_VERIFICATION = False
SOCIALACCOUNT_EMAIL_REQUIRED = False
LOGIN_REDIRECT_URL = '/'
ACCOUNT_ADAPTER = 'users.adapters.AccountAdapter'
SOCIALACCOUNT_ADAPTER = 'users.adapters.SocialAccountAdapter'
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = False
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'users.api.serializers.MobileLoginSerializer',
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation'
            '.UserAttributeSimilarityValidator'
        )
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation'
            '.MinimumLengthValidator'
        )
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation'
            '.CommonPasswordValidator'
        )
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation'
            '.NumericPasswordValidator'
        )
    },
]

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': [
            'email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {
            'auth_type': 'https'},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time'],
        'EXCHANGE_TOKEN': True,
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.4'
    },
    'linkedin': {
        'SCOPE': [
            'r_emailaddress',
        ],
        'PROFILE_FIELDS': [
            'id',
            'first-name',
            'last-name',
            'email-address',
            'picture-url',
            'public-profile-url',
        ]
    }

}

# thumbnails
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
        ('crop__280x280', 'crop__280x280'),
        ('crop__128x128', 'crop__128x128'),
        ('crop__44x44', 'crop__44x44'),
        ('crop__42x42', 'crop__42x42'),
    ]
}

# rest api
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': (
        'rest_framework.pagination'
        '.LimitOffsetPagination'
    ),
    'PAGE_SIZE': 10
}

SWAGGER_SETTINGS = {
    'JSON_EDITOR': False,
    'USE_SESSION_AUTH': True,
    'SHOW_REQUEST_HEADERS': True
}

# cache
CACHEOPS_REDIS = "redis://cache:6379/1"
CACHEOPS = {
    # Automatically cache any User.objects.get() calls for 15 minutes
    # This includes request.user or post.author access,
    # where Post.author is a foreign key to auth.User
    'auth.user': {'ops': 'get', 'timeout': 60 * 15},

    # Automatically cache all gets and queryset fetches
    # to other django.contrib.auth models for an hour
    'auth.*': {'ops': ('fetch', 'get'), 'timeout': 60 * 60},

    # Cache gets, fetches, counts and exists to Permission
    # 'all' is just an alias for ('get', 'fetch', 'count', 'exists')
    'auth.permission': {'ops': 'all', 'timeout': 60 * 60},

    # Enable manual caching on all other models with default timeout of an hour
    # Use Post.objects.cache().get(...)
    #  or Tags.objects.filter(...).order_by(...).cache()
    # to cache particular ORM request.
    # Invalidation is still automatic
    '*.*': {'ops': 'all', 'timeout': 60 * 60},
}
