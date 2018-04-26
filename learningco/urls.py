from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken import views as authviews
from django.conf.urls.static import static
from django.conf.urls import url, include
from learningco import settings  # noqa
from . import admin
from learningco.apps.users.api.views import \
    FacebookLogin, TwitterLogin, LinkedInLogin
from learningco.apps.users.views import UserHome


urlpatterns = [
    # django defaults
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),

    # REST framework and authentication
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    url(r'^rest-auth/linkedin/$', LinkedInLogin.as_view(), name='li_login'),
    url(r'^rest-auth/twitter/$', TwitterLogin.as_view(), name='twitter_login'),
    url(r'^api-token-auth/', authviews.obtain_auth_token),
    url(r'^docs/', get_swagger_view()),

    # api
    url(r'^api/', include(
        'learningco.apps.messaging.firebase.api.urls')),
    url(r'^api/', include(
        'learningco.apps.users.api.urls')),

    # web application
    url(r'^admin/', include(
        'learningco.apps.admin.urls', namespace='admin')),
    url(r'^companies/', include(
        'learningco.apps.companies.urls', namespace='companies')),
    url(r'^users/', include(
        'learningco.apps.users.urls', namespace='users')),

    url(r'^$', UserHome.as_view(), name='index'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

    if settings.LOCAL:
        urlpatterns += static(
            settings.STATIC_URL, document_root=settings.STATIC_ROOT)
