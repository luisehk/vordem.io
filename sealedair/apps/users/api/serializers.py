from rest_auth.serializers import LoginSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from ..models import Profile
from ...notifications.models.notifications import UserNotificationsConfig
from ...utils.serializers import BetterVersatileImageFieldSerializer

User = get_user_model()


class MobileLoginSerializer(LoginSerializer):
    pass


class ProfileSerializer(serializers.ModelSerializer):
    avatar = BetterVersatileImageFieldSerializer(sizes='profile_avatar')

    class Meta:
        model = Profile
        fields = [
            'id', 'avatar'
        ]


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name', 'last_name',
            'profile',
        ]
        read_only_fields = ['email']


class UserNotificationsConfigSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    filter_fields = ('user',)

    class Meta:
        model = UserNotificationsConfig
        fields = [
            'id', 'user_id', 'user', 'new_shipment', 'late_shipment',
            'delivered_shipment', 'email', 'sms',
        ]     
