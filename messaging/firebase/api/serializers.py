from django.contrib.auth import get_user_model
from rest_framework import serializers
from ..models import CustomDevice
from django.db.models import Q


User = get_user_model()


class DeviceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), default=1)
    reg_id = serializers.CharField()

    class Meta:
        model = CustomDevice
        fields = ('id', 'user', 'reg_id',)

    def validate_reg_id(self, value):
        # Don't validate anything. Let other functions replace old values
        return value

    def validate_user(self, value):
        # logged in user is the device owner
        request = self.context.get('request')
        user = request.user
        return user

    def delete_previous_devices(self, validated_data):
        # delete old devices or old users using this device
        CustomDevice.objects.filter(
            Q(reg_id=validated_data['reg_id']) |
            Q(user=validated_data['user'])
        ).delete()

    def set_active(self, instance):
        # mark device as active
        instance.is_active = True
        instance.save()
        return instance

    def create(self, validated_data):
        self.delete_previous_devices(validated_data)
        instance = super().create(validated_data)
        return self.set_active(instance)

    def update(self, instance, validated_data):
        self.delete_previous_devices(validated_data)
        instance = super().update(instance, validated_data)
        return self.set_active(instance)
