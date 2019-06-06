import os


SECRET_KEY = os.environ.get('SECRET_KEY', '0i324jsdfj9090u21nhio3')

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True
USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_HOST = True

SECURE_COOKIES = os.environ.get('SECURE_COOKIES', 'False').lower() == 'true'  # noqa
CSRF_COOKIE_SECURE = SECURE_COOKIES
CSRF_COOKIE_HTTPONLY = SECURE_COOKIES
SESSION_COOKIE_SECURE = SECURE_COOKIES
SESSION_COOKIE_HTTPONLY = SECURE_COOKIES

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
