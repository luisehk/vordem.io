from rest_framework import serializers
from ..models import Shipment, Comment, Status
from ...users.api.serializers import UserSerializer
from ...providers.serializers.carriers import TruckSerializer
from ...company.serializers.plants import PlantSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = [
            'id', 'user', 'datetime', 'body'
        ]


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'id', 'checkpoint', 'time_status',
            'start_datetime', 'end_datetime'
        ]


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
    truck = TruckSerializer()

    class Meta:
        model = Shipment
        fields = [
            'id', 'code',
            'truck', 'plant',
        ]
