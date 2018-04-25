from users.api.views import FacebookLogin, TwitterLogin, LinkedInLogin
from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken import views as authviews
from django.conf.urls.static import static
from django.conf.urls import url, include
from learningco import settings  # noqa
from . import admin


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

    # API
    url(r'^api/', include('messaging.firebase.api.urls')),
    url(r'^api/', include('users.api.urls')),

    # application
    url(r'^users/', include('users.urls', namespace='users')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    ) + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
