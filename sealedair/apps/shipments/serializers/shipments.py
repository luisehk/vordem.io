from rest_framework import serializers
from ..models import Shipment, Comment, Status
from ...users.api.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = [
            'user', 'datetime', 'body'
        ]


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'checkpoint', 'time_status',
            'start_datetime', 'end_datetime'
        ]


class ShipmentSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    status_history = StatusSerializer(many=True)
    current_status = StatusSerializer()

    class Meta:
        model = Shipment
        fields = [
            'carrier', 'plant', 'code', 'current_status',
            'start_datetime', 'arrival_datetime',
            'estimated_arrival_datetime', 'delay_reason',
            'comments', 'status_history'
        ]
