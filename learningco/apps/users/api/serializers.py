from versatileimagefield.serializers import VersatileImageFieldSerializer
from rest_auth.serializers import LoginSerializer
from django.contrib.auth import get_user_model
from fcm.utils import get_device_model
from rest_framework import serializers
from ..models import Profile
from ...score.serializers.scores import LeaderScoreSerializer
from ...companies.serializers.companies import CompanySerializer
from django.db.models import Q


Device = get_device_model()
User = get_user_model()


class MobileLoginSerializer(LoginSerializer):
    firetoken = serializers.CharField(required=False, allow_blank=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        user = attrs.get('user')

        firetoken = attrs.get('firetoken')
        if firetoken:
            devices = Device.objects.filter(reg_id=firetoken)
            if not devices.exists():
                device = Device(user=user, reg_id=firetoken, is_active=True)
            else:
                device = devices.first()
                device.user = user

            device.save()

            # cleanup the other devices
            Device.objects.filter(
                Q(user=user) | Q(reg_id=firetoken)
            ).exclude(
                id=device.id
            ).delete()

        return attrs


class ProfileSerializer(serializers.ModelSerializer):
    avatar = VersatileImageFieldSerializer(sizes='profile_avatar')
    generation = serializers.SerializerMethodField()
    level_of_hierarchy = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'id', 'avatar', 'position', 'generation', 'level_of_hierarchy'
        ]

    def get_generation(self, obj):
        return obj.get_generation_display()

    def get_level_of_hierarchy(self, obj):
        return obj.get_level_of_hierarchy_display()


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    leader_companies = CompanySerializer(many=True)
    leader_score = LeaderScoreSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name', 'last_name',
            'profile', 'leader_companies', 'leader_score',
        ]
        read_only_fields = ['email']
