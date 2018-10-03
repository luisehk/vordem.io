from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken import views as authviews
from django.conf.urls.static import static
from django.conf.urls import url, include
from allauth.account.views import confirm_email
from django.conf import settings
from . import admin

urlpatterns = [
    # admin platform
    url(r'^admin/', admin.site.urls),

    # django defaults
    url(r'^accounts/', include('allauth.urls')),

    # REST framework and authentication
    url(r'^rest-auth/registration/account-confirm-email/(?P<key>.+)/$',
        confirm_email, name='account_confirm_email'),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api-token-auth/', authviews.obtain_auth_token),
    url(r'^docs/', get_swagger_view()),

    # api
    url(r'^api/', include(
        'publicomex.apps.users.api.urls')),

    # web application
    url(r'^core/', include(
        'publicomex.apps.core.urls', namespace='core')),
    url(r'^directory/', include(
        'publicomex.apps.directory.urls', namespace='directory')),
    url(r'^notifications/', include(
        'publicomex.apps.notifications.urls', namespace='notifications')),
    url(r'^requests/', include(
        'publicomex.apps.requests.urls', namespace='requests')),
    url(r'^teams/', include(
        'publicomex.apps.teams.urls', namespace='teams')),
    url(r'^users/', include(
        'publicomex.apps.users.urls', namespace='users')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

    if not settings.USING_S3:
        urlpatterns += static(
            settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
        )

        if settings.LOCAL:
            urlpatterns += static(
                settings.STATIC_URL, document_root=settings.STATIC_ROOT)
