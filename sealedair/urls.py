from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken import views as authviews
from django.conf.urls.static import static
from django.conf.urls import url, include
from allauth.account.views import confirm_email
from sealedair.apps.users.views import UserHome
from django.conf import settings


urlpatterns = [
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
        'sealedair.apps.users.api.urls')),

    # web application
    url(r'^company/', include(
        'sealedair.apps.company.urls', namespace='company')),
    url(r'^providers/', include(
        'sealedair.apps.providers.urls', namespace='providers')),
    url(r'^shipments/', include(
        'sealedair.apps.shipments.urls', namespace='shipments')),
    url(r'^users/', include(
        'sealedair.apps.users.urls', namespace='users')),

    # home
    url(r'^$', UserHome.as_view(), name='index'),
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
