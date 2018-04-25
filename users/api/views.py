from allauth.socialaccount.providers.linkedin_oauth2.views import LinkedInOAuth2Adapter  # noqa
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter  # noqa
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from rest_auth.social_serializers import TwitterLoginSerializer
from rest_auth.registration.views import SocialLoginView
from rest_auth.views import LoginView
from django.contrib.auth.models import User
from users.api.serializers import UserSerializer, ProfileSerializer
from rest_framework.viewsets import ModelViewSet
from users.models import Profile


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class LinkedInLogin(SocialLoginView):
    adapter_class = LinkedInOAuth2Adapter


class TwitterLogin(LoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        u = self.request.user
        return super().get_queryset().filter(user=u)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        u = self.request.user.id
        return super().get_queryset().filter(id=u)
