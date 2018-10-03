REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'publicomex.apps.users.api.serializers.MobileLoginSerializer',  # noqa
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
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': (
        'rest_framework.pagination'
        '.LimitOffsetPagination'
    ),
    'PAGE_SIZE': 100000
}

SWAGGER_SETTINGS = {
    'JSON_EDITOR': False,
    'USE_SESSION_AUTH': True,
    'SHOW_REQUEST_HEADERS': True
}
