from rest_framework import serializers
from django.db import transaction
from ..models import Shipment, Comment, Status
from ...users.api.serializers import UserSerializer
from ...providers.serializers.carriers import (
    TruckSerializer, TruckCreationSerializer)
from ...company.serializers.plants import PlantSerializer
from ...providers.models import Truck
from django.contrib.auth import get_user_model


User = get_user_model()


# careful, only works if called from api requests...
# won't work inside celery tasks
def _add_current_user(serializer, validated_data):
    request = serializer.context.get('request')
    user = request.user

    extra_data = {'user': user}
    return {**validated_data, **extra_data}  # noqa


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Comment
        fields = [
            'id', 'shipment', 'user', 'datetime', 'body'
        ]

    def create(self, validated_data):
        data = _add_current_user(
            self, validated_data)
        return super().create(data)


class StatusSerializer(serializers.ModelSerializer):
    hours_since_start = serializers.SerializerMethodField()
    hours_since_shipment_departure = serializers.SerializerMethodField()
    checkpoint_display = serializers.SerializerMethodField()
    next_checkpoint = serializers.SerializerMethodField()
    previous_checkpoint = serializers.SerializerMethodField()
    time_status_display = serializers.SerializerMethodField()

    class Meta:
        model = Status
        fields = [
            'id', 'checkpoint', 'checkpoint_display',
            'next_checkpoint', 'previous_checkpoint',
            'time_status', 'time_status_display',
            'start_datetime', 'end_datetime',
            'hours_since_start', 'hours_since_shipment_departure']

    def get_hours_since_start(self, obj):
        return obj.get_hours_since_start()

    def get_hours_since_shipment_departure(self, obj):
        return obj.get_hours_since_shipment_departure()

    def get_checkpoint_display(self, obj):
        return obj.get_checkpoint_display()

    def get_next_checkpoint(self, obj):
        return obj.get_next_checkpoint()

    def get_previous_checkpoint(self, obj):
        return obj.get_previous_checkpoint()

    def get_time_status_display(self, obj):
        return obj.get_time_status_display()


class ShipmentSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    status_history = StatusSerializer(many=True)
    current_status = StatusSerializer()
    truck = TruckSerializer()
    plant = PlantSerializer()

    class Meta:
        model = Shipment
        fields = [
            'id', 'code', 'current_status',
            'start_datetime', 'arrival_datetime',
            'estimated_arrival_datetime', 'delay_reason',
            'truck', 'plant',
            'comments', 'status_history'
        ]


class ShipmentCreationSerializer(serializers.ModelSerializer):
    truck = TruckCreationSerializer()

    class Meta:
        model = Shipment
        fields = [
            'id', 'code',
            'truck', 'plant', 'start_datetime',
        ]

    def create(self, validated_data):
        truck = validated_data.pop('truck')

        with transaction.atomic():
            # create truck first
            truck, _ = Truck.objects.get_or_create(
                code=truck['code'],
                carrier=truck['carrier'])

            # now add it back to data
            return Shipment.objects.create(
                **{**validated_data, **{'truck_id': truck.id}}  # noqa
            )
